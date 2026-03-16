# PPE Detection Kit 🦺🪖

A lightweight **Personal Protective Equipment (PPE) Detection Web Application** that performs real-time object detection using a trained deep learning model and streams the results through a simple web interface.
The system connects to a live camera, runs inference on each frame, and displays detected PPE items such as **helmets, safety vests, gloves, or masks**.

This project is useful for **industrial safety monitoring**, **factory compliance checks**, and **AI vision demonstrations**.

---

## 📌 Features

* 🎥 **Live Camera Streaming**
* 🧠 **Real-time PPE Detection using YOLO**
* 🌐 **Simple Web Interface (Flask)**
* ⚡ **Lightweight and Fast Inference**
* 📦 Easy to deploy and customize
* 🔧 Works with **USB Camera or RTSP Camera**

---

## 🗂 Project Structure

```
PPE_Detection_Kit/
│
├── app.py                # Flask backend server
├── best.pt               # Trained PPE detection model
├── requirements.txt      # Python dependencies
│
└── templates/
     └── index.html       # Web interface
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/ppe-detection-kit.git
cd ppe-detection-kit
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv .venv
```

Activate environment:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / Mac**

```bash
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install flask ultralytics opencv-python
```

---

## ▶️ Running the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and go to:

```
http://localhost:5000
```

You will see a **live camera feed with PPE detection results**.

---

## 📷 Camera Configuration

### USB Camera (Default)

```python
camera = cv2.VideoCapture(0)
```

### RTSP Camera

```python
camera = cv2.VideoCapture("rtsp://username:password@camera_ip:port/stream")
```

---

## 🧠 Model

This project uses a **YOLO-based object detection model** trained for PPE detection.

Detected classes may include:

* Helmet
* Safety Vest
* Gloves
* Safety Glasses
* Mask
* No Helmet / No Vest (optional depending on training)

Replace `best.pt` with your trained model.

---

## 🚀 Future Improvements

Possible enhancements for production usage:

* 📊 PPE detection dashboard with counts
* 💾 Save violation snapshots
* 📡 RTSP multi-camera support
* 🔔 Alert system for PPE violations
* ⚡ ONNX / TensorRT acceleration
* 📱 Mobile-friendly UI

---

## 🛠 Technologies Used

* **Python**
* **Flask**
* **OpenCV**
* **Ultralytics YOLO**
* **HTML / CSS**

---

## 📄 License

This project is released under the **MIT License**.
You are free to modify and use it for personal or commercial applications.

---

## 👨‍💻 Author

Developed as a **computer vision safety monitoring system** for real-time PPE compliance detection.

---
