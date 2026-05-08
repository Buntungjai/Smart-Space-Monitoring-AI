# Smart Space Monitoring & Data Analytics System
### 🧠 AI-Powered Vision System for Facility Management

<div align="center">
  <img src="https://raw.githubusercontent.com/Buntungjai/Smart-Space-Monitoring-AI/main/BoundingBox.png" alt="AI Detection Demo" width="700">
</div>

**วิดีโอสาธิตการใช้งาน:** [Watch on YouTube](https://youtu.be/NTQSLex_IPo)

---

### 📌 Project Overview
พัฒนาระบบตรวจจับและวิเคราะห์ความหนาแน่นการใช้งานพื้นที่แบบ **Real-time** โดยใช้เทคโนโลยี AI เพื่อเปลี่ยนข้อมูลภาพจากกล้องวงจรปิดให้เป็นข้อมูลเชิงสถิติ (**Structured Data**) สำหรับนำไปใช้ในการบริหารจัดการทรัพยากรและพื้นที่ (Facility Management) อย่างมีประสิทธิภาพ

---

### 🛠️ Technology Stack

<p align="center">
  <img src="https://raw.githubusercontent.com/Buntungjai/Smart-Space-Monitoring-AI/main/device.png" width="450">
</p>

| Category | Technology | Description |
| :--- | :--- | :--- |
| **Hardware** | **NVIDIA Jetson Nano** | หน่วยประมวลผลหลักสำหรับ AI Inference |
| | **ESP32-CAM** | อุปกรณ์รับภาพต้นทางผ่าน HTTP Stream |
| **AI & Vision** | **SSD-Mobilenet-v2** | Deep Learning Model สำหรับ Object Detection |
| | **Jetson Inference** | Library สำหรับเพิ่มประสิทธิภาพการรัน AI บน GPU |
| | **OpenCV** | จัดการ Stream ข้อมูลภาพจาก Network Camera |
| **Back-end** | **Python** | ภาษาหลักในการพัฒนาระบบและ Logic |
| **Database** | **SQLite** | จัดเก็บข้อมูลการตรวจจับ (Logging) เพื่อทำ Analytics |

---

### ⚙️ Key Features (คุณสมบัติเด่น)

- **Autonomous Monitoring:** ตรวจจับบุคคลและอุปกรณ์สำนักงาน (Person, Keyboard, Laptop) ได้อัตโนมัติ และรองรับการขยายการตรวจจับวัตถุประเภทอื่นๆ
- **Data Persistence:** แปลงผลจาก AI ให้เป็นชุดข้อมูลในรูปแบบ **Relational Database (SQL)** เพื่อความสะดวกในการทำ Data Analytics ย้อนหลัง
- **Fault Tolerance:** ระบบ Reconnection Logic อัตโนมัติเมื่อสัญญาณภาพขัดข้อง เพื่อความต่อเนื่องของข้อมูล

---

### 💻 Data Architecture & Schema
ระบบจัดเก็บข้อมูลลงใน `detections.db` เพื่อนำไปพล็อตกราฟหรือวิเคราะห์ความหนาแน่นของพื้นที่ในแต่ละช่วงเวลา

<p align="center">
  <img src="https://raw.githubusercontent.com/Buntungjai/Smart-Space-Monitoring-AI/main/DBbrowser.jpg" width="600" alt="Database Schema">
</p>

**ตารางโครงสร้างข้อมูล (Detections Table):**

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | Integer | ลำดับรายการ (Primary Key) |
| `label` | String | ประเภทวัตถุที่ตรวจพบ (เช่น Person, Laptop) |
| `confidence`| Float | ค่าความเชื่อมั่นของ AI (0.0 - 1.0) |
| `timestamp` | DateTime | วันและเวลาที่ตรวจพบ (Local Time) |

---

### 🚀 Future Roadmap
- [ ] พัฒนา Dashboard ด้วย **Streamlit** หรือ **Grafana** เพื่อทำ Data Visualization
- [ ] เพิ่มระบบแจ้งเตือนผ่าน **Line Notify** เมื่อความหนาแน่นของคนเกินกำหนด
