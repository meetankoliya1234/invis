import cv2
import time
import numpy as np
from numpy.lib.type_check import imag

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

cap = cv2.VideoCapture(0)

time.sleep(5)
bg = 0

for i in range(60):
    ret, frame = cap.read()
    
frame = np.flip(frame, axis=1)

while(image.isOpened()):
    ret, image = cap.read()
    if not ret:
        break
    
    image = np.flip(image, axis = 1)
    
    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))

    u_black = np.array([104, 153, 70])
    l_black = np.array([30, 30, 0])

    mask = cv2.inRange(image, u_black, l_black)
    
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))
    