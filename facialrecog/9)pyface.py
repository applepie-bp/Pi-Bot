#import face_recognition
import pygame
from pygame.locals import *
import cv2
import numpy as np
import sys
import face_recognition

cascPath = "webca/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

folder = "webca/"
pic = "business.jpg"
pics= ["business.jpg", "trump.jpg"]
picpos = 0
#camera = cv2.VideoCapture(0) #capture video from webcam
pygame.init()
pygame.display.set_caption("OpenCV camera stream on Pygame")
#screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((800,800))

#init face_encodings
business_enc = face_recognition.load_image_file("webca/business.jpg")
trump_enc = face_recognition.load_image_file("webca/trump.jpg")


crashed = False
while not crashed:
    screen.fill([0,0,0])
    #frame = cv2.imread('webca/business.jpg')
    frame = cv2.imread(folder + pic)
    fw, fh = frame.shape[:2]
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    facesdet = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(20, 20),
        #flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    #
    #unknown_image = face_recognition.load_image_file(folder + pic, facesdet)

    #for all faces detected
    name = 0
    for (x, y, w, h) in facesdet:
        #cv2.imwrite("face" + str(name) + ".jpg", frame[y:y+h, x:x+w, ]) #saves detected faces to pic folder
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) # Draw a rectangle around the faces
        name = name + 1

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)
    frame = pygame.transform.flip(frame,True,False) #flip horizontally (mirror)
    screen.blit(frame, (0,0))

    dis = 0
    for (x, y, w, h) in facesdet:
        screen.blit(frame, (0 + dis ,fh - 100), (x , y, w, h))
        name = name + 1
        dis = dis + 100

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                picpos -= 1
                if picpos < 0:
                    picpos = 0
                pic = pics[picpos]
            if event.key == pygame.K_d:
                picpos += 1
                if picpos > len(pics) - 1:
                    picpos = len(pics) - 1
                pic = pics[picpos]
            if event.key == pygame.K_ESCAPE:
                crashed = True

pygame.quit() #close pygame
cv2.destroyAllWindows() #cv2 close
quit() #close python program
