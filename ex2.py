import os
import face_recognition
import numpy as np
from PIL import Image, ImageDraw
from picamera import PiCamera
from time import sleep
import serial
import time
import pickle
camera=PiCamera()
with open('encoding.pkl','rb') as f:
      known_face_encodings = pickle.load(f)
with open('names.pkl','rb') as f:
      known_face_names= pickle.load(f)

def image_recon():
# Load an image with an unknown face
    unknown_image = face_recognition.load_image_file("check.jpg")
    flag=0
# Find all the faces and face encodings in the unknown image
    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
# See http://pillow.readthedocs.io/ for more about PIL/Pillow
    pil_image = Image.fromarray(unknown_image)
# Create a Pillow ImageDraw Draw instance to draw with
    draw = ImageDraw.Draw(pil_image)

# Loop through each face found in the unknown image
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding,tolerance=0.4)

        name = "Unknown"

    # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

    # Draw a box around the face using the Pillow module
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    # Draw a label with a name below the face
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
        draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))
        print("pritning matches now")
        print(matches)
        for i in matches:
            print(i)
            if i==True:
                flag=1  
    print(flag)
    pil_image.save("intruder.jpg")
    if(flag==0):
        os.system('python send_email.py')
        os.system('python send_sms.py')
        
# Remove the drawing library from memory as per the Pillow docs
    del draw
ser =serial.Serial('/dev/ttyACM0',9600)
while 1:
    time.sleep(0.5)
    if(ser.in_waiting>0):
        line=ser.readline()
        l=str(line)
        print(l)
        if "ALERT" in l:
            camera.start_preview()
            sleep(5)
            camera.capture('/home/pi/Desktop/check.jpg')
            camera.stop_preview()
            image_recon()

      