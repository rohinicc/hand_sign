# 🖐️ Hand Sign Detection Using Python

This project is a real-time **hand sign detection system** built using **MediaPipe**, **OpenCV**, and **TensorFlow**. It detects specific hand signs and converts them to text and speech output. The goal is to bridge communication gaps by translating hand gestures into understandable words.

## 🚀 Features

- 🔍 Real-time hand sign detection using webcam
- 🧠 Sign recognition powered by TensorFlow models
- 🎤 Voice output using text-to-speech
- ⚙️ Easy-to-run Python script
- 📦 Uses OpenCV + MediaPipe for hand tracking

## 🛠️ Technologies Used

- **Python** 🐍
- **MediaPipe** (for hand landmark detection)
- **OpenCV** (for image processing)
- **TensorFlow** (for model prediction)
- **pyttsx3 / gTTS** (for speech output)

# 🖐️ Hand Sign Detection Using Python

Real-time hand sign recognition using Python, OpenCV, MediaPipe, TensorFlow and Text-to-Speech. Detects gestures via webcam and speaks the recognized sign.

🔗 GitHub: https://github.com/rohinicc/hand_sign

---

## ✅ Quick Setup Instructions (ALL-IN-ONE TERMINAL CODE)

Just copy and paste this whole thing into your terminal:

```bash
# Clone the project
git clone https://github.com/rohinicc/hand_sign.git
cd hand_sign

# (Optional) Create and activate virtual environment
python -m venv venv

# For Windows
venv\Scripts\activate

# For macOS/Linux
# source venv/bin/activate

# Install all required Python libraries
pip install opencv-python
pip install mediapipe
pip install tensorflow
pip install numpy
pip install pyttsx3

# If pyttsx3 doesn't work, use gTTS as backup
pip install gTTS playsound

# Run the app
python testvoice.py


