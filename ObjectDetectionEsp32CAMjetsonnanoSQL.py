print('Starting Work Table Monitor...')

import cv2
import jetson_inference
import jetson_utils
import time
import sqlite3 

# --- Database Setup ---
conn = sqlite3.connect('detections.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS logs 
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
              label TEXT, 
              confidence REAL, 
              timestamp DATETIME)''')
conn.commit()

# --- AI & Camera Setup ---
input_url = "http://10.0.30.106:81/stream"
net = jetson_inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
display = jetson_utils.videoOutput("display://0")
camera = cv2.VideoCapture(input_url)

# --- Configuration ---
target_objects = ['person', 'cell phone', 'keyboard', 'laptop', 'bottle']
save_interval = 2.0 
last_save_time = time.time()

def get_camera(url):
    print("Connecting to ESP32-CAM at {}...".format(url))
    return cv2.VideoCapture(url)

camera = get_camera(input_url)

try:
    while display.IsStreaming():
        ret, frame = camera.read()
        
        if not ret:
            print("Stream interrupted. Attempting to reconnect...")
            camera.release()
            time.sleep(1) # Wait a second before retrying
            camera = get_camera(input_url)
            continue # Go back to the start of the loop

        # --- AI Processing ---
        img_rgba = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        cuda_mem = jetson_utils.cudaFromNumpy(img_rgba)
        detections = net.Detect(cuda_mem)

        # --- SQL Logging ---
        current_time = time.time()
        if detections and (current_time - last_save_time > save_interval):
            for detection in detections:
                class_name = net.GetClassDesc(detection.ClassID)
                if class_name in target_objects:
                    c.execute("INSERT INTO logs (label, confidence, timestamp) VALUES (?, ?, datetime('now', 'localtime'))", 
                              (class_name, detection.Confidence))
                    conn.commit()
                    print("Logged: {}".format(class_name))
            last_save_time = current_time

        display.Render(cuda_mem)
        display.SetStatus("Monitoring Table | {:.0f} FPS".format(net.GetNetworkFPS()))

except KeyboardInterrupt:
    print("\nUser stopped the script.")
finally:
    camera.release()
    conn.close()
