#pylint:disable=no-member

import cv2 as cv

img = cv.imread('../Resources/Photos/lady.jpg')
cv.imshow('Group of 5 people', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray People', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

''' 
minNeighbors : Parameter specifying how many neighbors each candidate rectangle should have to retain it. 
    This parameter will affect the quality of the detected faces: higher value results in less detections but with higher quality 
scaleFactor — Parameter specifying how much the image size is reduced at each image scale. Basically, the scale factor
    is used to create your scale pyramid.More explanation, your model has a fixed size defined during training, 
    which is visible in the XML. This means that this size of the face is detected in the image if present. However, by rescaling the input image,
    you can resize a larger face to a smaller one, making it detectable by the algorithm. 1.05 is a good possible value for this, 
    which means you use a small step for resizing, i.e. reduce the size by 5%, you increase the chance of a matching size with the model for detection is found.
    This also means that the algorithm works slower since it is more thorough. You may increase it to as much as 1.4 for faster detection,
    with the risk of missing some faces altogether. In our case, I have used 1.0485258 as the scaleFactor as this worked perfectly for the image that I was using.
'''
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3) # return rectangular coordinates of the face

print(f'Number of faces found = {len(faces_rect)}')

print (faces_rect)

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)



cv.waitKey(0)