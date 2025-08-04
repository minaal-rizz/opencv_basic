#COLORS AND COLOR DETECTION

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break  # if frame is not captured properly, skip the loop

    width = int(cap.get(3))  # Property ID 3 = width
    height = int(cap.get(4))  # Property ID 4 = height

    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #convert to saturation and lightness in bgr
    lower_blue=np.array([90,50,50])
    upper_blue=np.array([130,255,255])

    #pt of frame (which pixels are in lower n upper blue)
    mask=cv2.inRange(hsv,lower_blue, upper_blue)
    result=cv2.bitwise_and(frame, frame, mask=mask)

    
    cv2.imshow('frame', result)
    cv2.imshow('frame', mask)

    if cv2.waitKey(1)==ord('q'):
        break

BGR_color = np.uint8([[[255, 0, 0]]])  # Blue in BGR
HSV_color = cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV)  
print("HSV value of pure blue:", HSV_color)
