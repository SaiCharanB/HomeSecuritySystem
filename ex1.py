import os
import face_recognition
import numpy as np
from PIL import Image, ImageDraw
from picamera import PiCamera
from time import sleep
import serial
import time
import pickle


sujay = face_recognition.load_image_file("sujay.jpg")
sujay_encoding = face_recognition.face_encodings(sujay)[0]

sai = face_recognition.load_image_file("sai.jpg")
sai_encoding = face_recognition.face_encodings(sai)[0]

neil = face_recognition.load_image_file("neil.jpg")
neil_encoding = face_recognition.face_encodings(neil)[0]

saichi = face_recognition.load_image_file("saichi.jpg")
saichi_encoding = face_recognition.face_encodings(saichi)[0]

known_face_encodings = [
    sujay_encoding,sai_encoding ,neil_encoding ,saichi_encoding   #array with all family encodings
]
known_face_names = [
    "Sujay",
    "sai",
    "neil",
    "saichi"#array with all corresponding name , a[i] to b[i] relation
]
with open('encoding.pkl','wb') as f:
    pickle.dump(known_face_encodings, f)  
with open('names.pkl','wb') as f:
    pickle.dump(known_face_names,f)
    

    
