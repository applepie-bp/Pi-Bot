import urllib.request
import cv2
import sys
import logging as log
import datetime as dt
import time

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)

video_capture = cv2.VideoCapture(0)
anterior = 0

while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        time.sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()
	#print(frame.shape)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    for face in faces:
        print(face)
        if face[0]< 640*0.33333:
            print("Left")
            response = urllib.request.urlopen("http://localhost:5000/leftturn")
            time.sleep(0.5)
        elif face[0]< 640*0.666666:
            print("Middle")
            response = urllib.request.urlopen("http://localhost:5000/forward")
            time.sleep(0.5)
        else:
            print("Right")
            response = urllib.request.urlopen("http://localhost:5000/rightturn")
            time.sleep(0.5)
            
    response = urllib.request.urlopen("http://localhost:5000/dist")
    response_text = response.read()
    if float(response_text)<15:
        response = urllib.request.urlopen("http://localhost:5000/stop")
        print("Something is in the way!")
    # Draw a rectangle around the faces
   # for (x, y, w, h) in faces:
     #   cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #if anterior != len(faces):
        # anterior = len(faces)
        # log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))


    # Display the resulting frame
    # cv2.imshow('Video', frame)


    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

    # Display the resulting frame
    # cv2.imshow('Video', frame)

# When everything is done, release the capture
response = urllib.request.urlopen("http://localhost:5000/stop")
video_capture.release()
cv2.destroyAllWindows()
