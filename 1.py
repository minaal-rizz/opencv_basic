#INTRO AND IMGS

import cv2 

img=cv2.imread('imgs/image.png',0 )
#to re size img: 
img=cv2.resize(img, (500,500))
img= cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite('new.png', img) #making new file of this 

#mode to load img (coloured/geyscale/w.o transparency)
'''| Mode      | Flag                           | Description                                                                    |
| --------- | ------------------------------ | ------------------------------------------------------------------------------ |
| Color     | `cv2.IMREAD_COLOR` or `1`      | Loads image in **color**. Ignores transparency (alpha) channel. *(Default)*    |
| Grayscale | `cv2.IMREAD_GRAYSCALE` or `0`  | Loads image in **grayscale** (1 channel only).                                 |
| Unchanged | `cv2.IMREAD_UNCHANGED` or `-1` | Loads image **as-is**, including **alpha transparency** (e.g., PNG with RGBA). |
'''

cv2.imshow('Image', img)
cv2.waitKey(0) #0 means  wait infinitely 
cv2.destroyAllWindows()



