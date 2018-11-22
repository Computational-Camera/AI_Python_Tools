import cv2
import numpy as np
import face_recognition   #dlib?

face_locations    = []
db_face_encodings = []
# Load the jpg file into a numpy array
image = face_recognition.load_image_file("./1.jpg")
face_locations = face_recognition.face_locations(image, model="cnn")#
face_encodings = face_recognition.face_encodings(image, face_locations)
db_face_encodings.append(face_encodings[0].ravel()) #128 size vector

db_array = np.asarray(db_face_encodings) # YOU CAN THEN SAVE IT TO DATABASE

for face_location in face_locations:
    top, right, bottom, left = face_location
    cv2.rectangle(image,(left,top),(right,bottom),(196,32,32),1)
   
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)    

face_landmarks = face_recognition.face_landmarks(image)
print(face_landmarks)

cv2.imwrite('face.png', image )
