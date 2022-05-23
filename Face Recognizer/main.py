import  os
import  cv2 as cv
import  numpy as np


people = []
for i in os.listdir(r'W:\Python\opencv-course-master\Resources\Faces\train'):
    people.append(i)

print(people)

DIR = r'W:\Python\opencv-course-master\Resources\Faces\train'

haar_cascade = cv.CascadeClassifier('res/haar_face.xml')


features = []
labels = []
def create_train():
    for person in people:

        path = os.path.join(DIR, person) # print(path) >  W:\Python\opencv-course-master\Resources\Faces\train\Ben Afflek
        label = people.index(person) # print(label) >  total number of files  5

        for img in os.listdir(path):

            img_path = os.path.join(path, img) # acceess to every single image inside the 5 folder
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor= 1.1, minNeighbors= 4)
            '''
            detectMultiScale(gray, 1.3, 5) MultiScale detects objects of different sizes in the input image.
            returns rectangles positioned on the faces. (x,y,w,h)
            '''

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y: y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


create_train()
print("Training done")
# now we are going to train our recongnizer

features = np.array(features,dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)

face_recognizer.save('res/face.yml') # create yml file to get the training data

np.save("features.npy", features)
np.save("labels.npy", labels)
