import os
import face_recognition
import numpy as np
from PIL import Image, ImageDraw
from picamera import PiCamera
from time import sleep
import serial
import time
import pickle
with open('encoding.pkl','rb') as f:
      known_face_encodings = pickle.load(f)
with open('names.pkl','rb') as f:
      known_face_names= pickle.load(f)


camera=PiCamera()

def add_face():
    name=input("Input new members name")
    print("Please stand in front of the camera")
    camera.start_preview()
    sleep(5)
    loc = name+".jpg"
    camera.capture(loc)
    camera.stop_preview()
    f=0 #f=0 means nigga is guest,f=1 means nigga is family
    g_days=0 #no of days a guest stays 
    img="saiptest.jpg" #all images stored as saip test
    new_face=face_recognition.load_image_file(img)
    new_face_encoding=face_recognition.face_encodings(new_face)[0]
    known_face_encodings.append(new_face_encoding)
    known_face_names.append(name)
def del_face():
    n=input("Enter name to be removed")
    print(known_face_names)
    index=0
    i=0
    if(n in known_face_names):
        print("Name is present")
    else:
        exit(0)
    for i in range(len(known_face_names)):
        if(known_face_names[i]==n):
            index=i  
    known_face_names.remove(n)
    known_face_encodings.pop(index)
    print("Updated list of residents")
    print(known_face_names)
choice=int(input("Press \n1.Continue \n2.Exit\n"))



while(choice==1):
    print("1)Add face")
    print("2)Delete face")
    print("3)Save and exit")
    print("4)Display residents")
    ch=int(input("Enter choice"))
    if(ch==1):
        add_face()
    elif(ch==2):
        del_face()
    elif(ch==3):
        with open('encoding.pkl','wb') as f:
            pickle.dump(known_face_encodings, f)  
        with open('names.pkl','wb') as f:
            pickle.dump(known_face_names,f)
            break
    elif(ch==4):
        for i in  known_face_names:
            print(i)
    choice=int(input("Press 1.Continue \n2.Exit"))
