import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import time
import pyttsx3  # Import the text-to-speech library

# Initialize text-to-speech engine
engine = pyttsx3.init()

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
model_path = "C://Users/bharathi/OneDrive/Desktop/hand_sign/Model/converted_keras/keras_model.h5"
label_path = "C://Users/bharathi/OneDrive/Desktop/hand_sign/Model/converted_keras/labels.txt"
classifier = Classifier(model_path, label_path)
offset = 20
imgSize = 300
folder = "C:/Users/bharathi/OneDrive/Desktop/hand_sign/data/Z"
counter = 0
labels = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

while True:
    success, img = cap.read()
    imgOutput = img.copy()
    hands, img = detector.findHands(img)
    
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
        imgCropShape = imgCrop.shape
        aspectRatio = h / w
        
        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap:wCal + wGap] = imgResize
            prediction, index = classifier.getPrediction(imgWhite)
            print(prediction, index)
        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize
            prediction, index = classifier.getPrediction(imgWhite)
        
        # Add voice output for the detected hand sign
        detected_sign = labels[index]
        engine.say(detected_sign)  # Speak the detected sign
        engine.runAndWait()
        cv2.rectangle(imgOutput, (x - offset, y - offset-50), (x-offset+100, y-offset-50+50), (0, 255, 0), cv2.FILLED)
        cv2.putText(imgOutput, labels[index], (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 2)
        cv2.imshow("ImgCrop", imgCrop)
        cv2.imshow("ImgWhite", imgWhite)
        cv2.rectangle(imgOutput, (x - offset, y - offset), (x + w + offset, y + h + offset), (0, 255, 0),4)
        cv2.imshow("image white",imgWhite)
    cv2.imshow("Image", imgOutput)   
    cv2.waitKey(1)