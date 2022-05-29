import cv2 as cv
import numpy as np

face_cascade = cv.CascadeClassifier('haar_face.xml')

capture = cv.VideoCapture(0)
while 1:
    ret,img = capture.read()
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 11)

    for (x,y,w,h) in faces:
        cv.rectangle(img, (x,y),(x+w,y+h), (255,255,0),thickness=1)
    
    if ret:    
        cv.imshow('Video', img)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()
