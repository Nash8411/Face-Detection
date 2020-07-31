#this is for the video image detection
import cv2
from random import randrange

# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#choose an image to detect faces in 
#img = cv2.imread('RNJ.jpg')

#to capture the video from the webcam here (0) means the default webcam
webcam = cv2.VideoCapture(0)

#Iterating forever over frames till webcam closes 
while True:
    successful_frame_read, frame = webcam.read()

    #must convert in grayscale
    #in opencv colors work backwords i.e insted of RGB they are BGR
    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscale_img)

    #to draw the rectangle
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256), randrange(256) , randrange(256)),2)


    #dispaly the colored frame
    cv2.imshow('Nash vaz face detector',frame)
    #it is used to display if u don't use a wait key the webcam won't display and (1) is 1 Milisec(time)
    key = cv2.waitKey(1) 
  

    #To stop if Q is pressed  81 and 113 are the ascii codes of q & Q
    if key==113 or key==81:
        break

#release the webcam object
webcam.release()

print("\n code completed")

"""
# Detect faces
# detectMultiScale used to detect objects i.e  faces  of any sizes and return the coordinatesof the rectangle its a classifier
face_coordinates = trained_face_data.detectMultiScale(grayscale_img)

#Draw rectangle around the faces
# now here (91,25,83,83) this were the coordinates ,(0,0,255)- this is the color which is red  , and that 2 is the tickness of the rectangle 
#cv2.rectangle(img,(91,25),(91+83,25+83), (0,0,255),2)

# here we are taking the coordinates dyanamically ie no hard coding but it will only detect one person form the frame but  if there are two people in a single frame we can chenge the face_coodinates[1]
#[x,y,w,h] = face_coordinates[0]

#now we are using for loop
#randrange gives a random color everytime

for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img,(x,y),(x+w,y+h), (randrange(256),randrange(256) ,randrange(256)),2)

#print(face_coordinates)
#this was the cooidinates shown [[91 25 83 83]]

#Display the image with the faces
cv2.imshow('Nash vaz face detector',img)
cv2.waitKey()

print("code completed")

"""