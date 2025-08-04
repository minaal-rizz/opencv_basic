
#IMAGE FUNDAMENTALS AND MANIPULATION



import cv2 
import random
imageee=cv2.imread('imgs/img.jpeg', -1)
imageee=cv2.resize(imageee,(500,500))

blurred_image= cv2.GaussianBlur(imageee, (5,5), 0)
cv2.imshow('blurr', blurred_image)
print (type(imageee))
print (imageee.shape) #height width and channel (pixels)
print (imageee)
print (imageee[0])
for i in range (100):
    for j in range(imageee.shape[1]):
        imageee[i][j]=[random.randint(0,255),random.randint(0,255), random.randint(0,255)]
cv2.imshow('image', imageee)
cv2.waitKey(0)
cv2.destroyAllWindows()     
