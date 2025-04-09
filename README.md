# 🖐️ Hand Sign Detection Using Python

This project is a real-time **hand sign detection system** built using **MediaPipe**, **OpenCV**, and **TensorFlow**.  
It detects specific hand signs and converts them to **text** and **speech output**.  
The goal is to bridge communication gaps by translating hand gestures into understandable words.

---

## 🚀 Features

- 🎥 **Real-time** hand sign detection via webcam  
- 🧠 **Gesture recognition** powered by trained TensorFlow models  
- 🗣️ **Text-to-Speech output** using pyttsx3 or gTTS  
- 💻 Lightweight Python script, easy to run  
- 🖐️ Hand tracking using OpenCV + MediaPipe

---

## 🛠️ Technologies Used

| 🔧 Tech        | 💡 Description                             |
|---------------|---------------------------------------------|
| 🐍 **Python**     | Core programming language                |
| 🪞 **MediaPipe**  | Hand landmark detection and tracking     |
| 🎞️ **OpenCV**     | Image processing & webcam capture        |
| 🧠 **TensorFlow** | ML model to recognize hand signs         |
| 🔊 **pyttsx3** / 🔈 **gTTS** | Converts predicted text to speech       |

---

🔗 **GitHub:**  
👉 [https://github.com/rohinicc/hand_sign](https://github.com/rohinicc/hand_sign)

---

## ✅ Quick Setup Instructions (ALL-IN-ONE TERMINAL CODE)

Copy-paste this entire block into your terminal and you're ready to roll:

```bash
# 🚀 Clone the project
git clone https://github.com/rohinicc/hand_sign.git
cd hand_sign

# 🛡️ (Optional) Create and activate a virtual environment
python -m venv venv

# ▶️ For Windows
venv\Scripts\activate

# ▶️ For macOS/Linux
# source venv/bin/activate

# 📦 Install required packages
pip install opencv-python
pip install mediapipe
pip install tensorflow
pip install numpy
pip install pyttsx3

# 🔁 Optional: If pyttsx3 doesn't work for TTS, use gTTS instead
pip install gTTS playsound

# 🎯 Run the main script
python testvoice.py
