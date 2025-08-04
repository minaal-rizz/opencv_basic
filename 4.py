#DRAWING (LINES, CIRCLES, RECT, TEXT)
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break  # if frame is not captured properly, skip the loop

    # Get the dimensions of the frame
    width = int(cap.get(3))  # Property ID 3 = width
    height = int(cap.get(4))  # Property ID 4 = height

    img=cv2.line(frame, (0,0),( width, height),(255,0,0), 50) 
    img=cv2.line(img, (0,height),( width, 0),(0,255,0), 5)  #diagnol line
    img=cv2.circle(img, (300,300), 60, (0,0,255), -1)
    img=cv2.rectangle(img, (100, 100), (200,200), (128,128,128), 10) #grey rect
    
    font=cv2.FONT_HERSHEY_COMPLEX
    img=cv2.putText(img, 'Minaal the great', (200,height-10), font, 2,  (0,0,0), cv2.LINE_AA, 3) #black text, bottom left. 3 thickness, 2 size of font

    
    cv2.imshow('frame', img)

    if cv2.waitKey(1)==ord('q'):
        break