import numpy as np
import cv2
import matplotlib.pyplot as plt


def detect_face(img):
    face_img = img.copy()

    face_rects = face_cascade.detectMultiScale(face_img)

    for (x, y, w, h) in face_rects:
        cv2.rectangle(face_img, (x, y), (x + w, y + h), (255, 255, 255), 10)

    return face_img


def adj_detect_face(img):
    face_img = img.copy()

    face_rects = face_cascade.detectMultiScale(face_img, scaleFactor=1.07, minNeighbors=5)

    for (x, y, w, h) in face_rects:
        cv2.rectangle(face_img, (x, y), (x + w, y + h), (255, 255, 255), 5)

    return face_img


def live_detection_by_camera():
    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read(0)

        frame = detect_face(frame)

        cv2.imshow('Video Face Detection', frame)

        c = cv2.waitKey(1)
        # Esc key
        if c == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


einstein = cv2.imread('data/albert_einstein.jpg', 0)
solvay_conference = cv2.imread('data/solvay_conference.jpg', 0)

face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_alt.xml')

# plt.imshow(einstein, cmap='gray')
# plt.show()

result = adj_detect_face(solvay_conference)
plt.imshow(result, cmap='gray')
plt.show()

live_detection_by_camera()