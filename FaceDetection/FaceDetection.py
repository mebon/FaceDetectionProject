import cv2

face_cascade = cv2.CascadeClassifier('C:/Users/bekom/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
resimler = ['images/futbol.jpg','images/groupSelfie.jpg','images/manzara.jpg']

for i in resimler:

    image = cv2.imread(i)

    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #cv2.COLOR_BGR2GRAY , cv2.COLOR_BGR2RGB

    faces = face_cascade.detectMultiScale(grayImage, 1.10, 6)
    #face_cascade.detectMultiScale(self, image, scaleFactor=None, minNeighbors=None, flags=None, minSize=None, maxSize=None)

    #print(type(faces)) #-> <class 'numpy.ndarray'>

    if len(faces) == 0:
        print( "Yuz bulunmadi.")

    else:
        print(faces)
        print(faces.shape)
        print("Bulunan Yuz Sayisi: " + str(faces.shape[0]))

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.rectangle(image, ((0, image.shape[0] - 25)), (270, image.shape[0]), (255, 255, 255), -1)
        cv2.putText(image, "Bulunan Yuz Sayisi: " + str(faces.shape[0]), (0, image.shape[0] - 10), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 0), 1)

        cv2.imshow('Yuz Tanima', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
