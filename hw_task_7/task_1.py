"""
1.	Создайте класс для лиц, с фото и видео.
a.	В классе должны быть следующие методы:
i.	Метод предобработки фото, видео (путь получаем при инициализации) - метод загружает фото, или видео
ii.	Метод детекта
iii.	Метод инференса
iv.	Метод отображения
b.	Также сделайте возможность изменять размеры отображаемого фото, видео, при вызове метода.
"""

import cv2

class FaceRecognition:
    def __init__(self, path):
        self.path = path
        self.preprocess()

    def preprocess(self):
        if self.path.endswith('.jpg') or self.path.endswith('.png'):
            self.pic = cv2.imread(self.path)
        elif self.path.endswith('.mp4') or self.path.endswith('.avi'):
            self.vid = cv2.VideoCapture(self.path)

    def detect(self):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(self.pic, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        return faces

    def infer(self):
        faces = self.detect()
        for (x, y, w, h) in faces:
            cv2.rectangle(self.pic, (x, y), (x + w, y + h), (0, 0, 255), 2)

    def display(self, width=None, height=None):
        if self.pic is not None:
            if width or height:
                h, w = self.pic.shape[:2]
                if width is None:
                    ratio = height / h
                    dimension = (int(w * ratio), height)
                else:
                    ratio = width / w
                    dimension = (width, int(h * ratio))

                self.pic = cv2.resize(self.pic, dimension)
            cv2.imshow('image', self.pic)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif self.video is not None:
            while True:
                ret, frame = self.vid.read()
                if ret:
                    if width and height:
                        frame = cv2.resize(frame, (width, height))
                    cv2.imshow('video', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break
            self.vid.release()
            cv2.destroyAllWindows()

face = FaceRecognition('test.jpg')

face.infer()
face.display(None, 800)