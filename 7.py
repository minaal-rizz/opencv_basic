#TEMPLATE MATCHING (detecting img in another )
#OBJECT DETECTION


'''cv2.TM_CCOEFF
Correlation Coefficient - Measures how well the template correlates with the image patch (ignores brightness). Higher = better match.
cv2.TM_CCOEFF_NORMED
Normalized Correlation Coefficient - Same as above but normalized to range [-1, 1] for brightness invariance. Closer to 1 = better match.
cv2.TM_CCORR
Cross-Correlation - Measures direct similarity between template and patch (sensitive to brightness). Higher = better match.
cv2.TM_CCORR_NORMED
Normalized Cross-Correlation - Same as above but normalized, so it's more robust to lighting changes. Higher = better match.
cv2.TM_SQDIFF
Squared Difference - Measures pixel-by-pixel error (lower means more similar). Lower = better match.
cv2.TM_SQDIFF_NORMED
Normalized Squared Difference - Same as above but normalized for consistent scale. Closer to 0 = better match.

'''
import numpy as np 
import cv2 

img=cv2.imread('imgs/match.jpg')
template=cv2.imread('imgs/ball.png')
img2=img.copy()

h, w= template.shape[:2]

methods=[cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, 
         cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2= img.copy() 

    result=cv2.matchTemplate(img2, template, method) #convultional happens, taking the img and sliding around base img to check match in region. 
    #get enoer 2d arrray to tell hoe much matching there is in the pics
    min_val, max_val, min_loc, max_loc=cv2.minMaxLoc(result)  #return min max val and loc in array
    print (min_loc, max_loc)
    
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location=min_loc 
    else:
        location=max_loc

    bottom_right=(location[0]+w, location[1]+h)
    cv2.rectangle(img2, location, bottom_right, 255,5)
    cv2.imshow('Match', img2) #method 3 didnt identify well (cv2.TM_CCORR)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
