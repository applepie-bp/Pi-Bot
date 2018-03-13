import time
start = time.time()
import face_recognition
import cv2
import os
import sys

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
#fs = ["webca/business.jpg", "webca/trump2.jpg"]
#business_img = face_recognition.load_image_file("webca/business.jpg")
#trump_img = face_recognition.load_image_file("webca/trump2.jpg")
#business_enc = face_recognition.face_encodings(business_img)[0]
#trump_enc = face_recognition.face_encodings(trump_img)[0]

known_faces = []
known_names = []

directory = os.fsencode("faceData")
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".jpg"):
        current_img = face_recognition.load_image_file("faceData/" + filename)
        current_enc = trump_enc = face_recognition.face_encodings(current_img)[0]
        known_faces.append(current_enc)
        known_names.append(filename)


#known_faces.append(trump_enc)

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

setup = time.time() - start
print("setup time: " + str(setup))

crashed = False
while crashed == False:
    f_start = time.time()
    # Grab a single frame of video
    #frame = video_capture.read()
    frame = cv2.imread(str(sys.argv[1]))
    small_frame = frame
    # Resize frame of video to 1/4 size for faster face recognition processing
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)[0]

        face_names = []
        # See if the face is a match for the known face(s)
        #match = face_recognition.face_distance(known_faces, face_encoding)
        match = face_recognition.compare_faces(known_faces, face_encodings)
        name = "Unknown"

        for x in range(0,len(match)):
            if match[x] == True:
                name = known_names[x]
        #if match[1] == True:
        #    name = "Trump"

        face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        centerhor = (left + right)/2
        centerver = (top + bottom)/2
        print("center: "+str(centerhor) + ", "+ str(centerver))

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 20), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
        #draws label for center
        cv2.circle(frame, (int(centerhor),int(centerver)), 10, (0,255,0), -1)
        h, w, c = frame.shape

        #vector from face to the center of the image
        print(round((w/2)-centerhor,2))
        print(round((h/2)-centerver,2))

    # Display the resulting image
    cv2.imshow("Face Recognition", frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    f_end = time.time() - f_start
    print("frame took " + str(f_end))

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
