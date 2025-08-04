#CORNER DETECTION

import numpy as np
import cv2

img = cv2.imread('imgs/chess.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


img2=img.copy()

corners = cv2.goodFeaturesToTrack(gray, maxCorners=50, qualityLevel=0.2 , minDistance=30)

corners = np.int32(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

# Draw lines between each pair of corners
for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
                #sp func applied to all. apply to array and return new array. map all values to func and convert to func
        color = tuple(map(int, np.random.randint(0, 255, size=3)))  # Random BGR color
        cv2.line(img, corner1, corner2, color, 1)

# Show result
cv2.imshow('Corners and Connections', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
