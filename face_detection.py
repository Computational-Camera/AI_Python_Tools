import cv2
import numpy as np
import face_recognition   #dlib?

face_locations = []

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("./1.jpg")
face_locations = face_recognition.face_locations(image, model="cnn")#

for face_location in face_locations:
    top, right, bottom, left = face_location
    cv2.rectangle(image,(left,top),(right,bottom),(196,32,32),1)
   
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)    

face_landmarks = face_recognition.face_landmarks(image)
print(face_landmarks)

cv2.imwrite('face.png', image )
