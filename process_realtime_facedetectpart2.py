"""
ECE196 Face Recognition Project
Author: W Chen

Adapted from:
http://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/

Use this code as a template to process images in real time, using the same techniques as the last challenge.
You need to display a gray scale video with 320x240 dimensions, with box at the center
"""


# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

face_cascade = cv2.CascadeClassifier('/home/pi/opencv-2.4.13.4/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    img2=cv2.resize(img,None, fx=0.25,fy=0.25)
    faces = face_cascade.detectMultiScale(img2, 1.3, 5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img2,(x,y),(x+w,y+h),(255, 255, 255),2)

    # show the frame
    cv2.imshow("Frame", img2)
    key = cv2.waitKey(1) & 0xFF
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    from random import randint
    if key == ord('c'):
        crop_img=img[4*y:4*(y+h), 4*x:4*(x+w)]
        cv2.imwrite('/home/pi/Desktop/faceimages/image%s.jpg' % randint(1000, 2000),crop_img)
    if key == ord("q"):
        break

