import  os
import  cv2 as cv

people = []
for i in os.listdir(r'W:\Python\opencv-course-master\Resources\Faces\train'):
    people.append(i)

haar_cascade = cv.CascadeClassifier('res/haar_face.xml')

face_recogniz = cv.face.LBPHFaceRecognizer_create()
face_recogniz.read('res/face.yml') # reads the yml file

img = cv.imread(r'W:\Python\opencv-course-master\Resources\Faces\val\elton_john\1.jpg') # selecting the pictuire

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Person', gray)

face_react = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in face_react:

    faces_roi = gray[y: y + h, x:x + w] # detect the face ratio
    label, confidence = face_recogniz.predict(faces_roi) # gets the name
    print(f'{people[label]} with a confidence of {confidence}')
    cv.putText(img, str( people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness= 2 )
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness= 2)

cv.imshow('Deteceted face', img)
cv.waitKey(0)

