import cv2
import sys

cascPath = "webca/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
#video_capture = cv2.VideoCapture(0)

#while cv2.getWindowProperty('Face detect', 0) < 100:
while True:
    # Capture frame-by-frame
    #ret, frame = video_capture.read()
    #print(cv2.getWindowProperty('Face detect', 0))
    frame = cv2.imread('webca/business.jpg')

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        #flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face detect', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
#video_capture.release()
cv2.destroyAllWindows()
