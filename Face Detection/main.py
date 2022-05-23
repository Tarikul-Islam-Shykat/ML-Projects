import cv2 as cv
img = cv.imread('res/group2.jpg')
#cv.imshow("People",img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("Gray Person",gray)

haar_cascade = cv.CascadeClassifier('res/haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=2.3, minNeighbors=3)
'''
this will take an image and use this variable for scale factor and minimum label to essentialyy
detect a face and return the rectangular co-ordinates of that face as a list .
This function will return a rectangle with coordinates(x,y,w,h) around the detected face. 
'''

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)


'''
haar case_cade can be prone to noise. By changing the value of scaleFactor and minNegihbors
you can mimimize the noises and detece the actual face


'''
cv.imshow('Detected Faces', img)
cv.waitKey(0)
