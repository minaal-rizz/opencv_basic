#CAMERA AND VIDEO CAPTURE 
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

    # Create a black canvas of the same shape as the frame
    image = np.zeros(frame.shape, np.uint8)

    # Resize the frame to half its size
    smaller_frame = cv2.resize(frame, (width // 2, height // 2))

    # Place the smaller frame in all 4 quadrants
    
        # Top-left quadrant: place the smaller_frame
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)

    # Bottom-left quadrant: place the same smaller_frame
    image[height//2:, :width//2] = smaller_frame

    # Top-right quadrant: place the same smaller_frame
    image[:height//2, width//2:] = smaller_frame

    # Bottom-right quadrant: place the same smaller_frame
    image[height//2:, width//2:] = smaller_frame

    # Show the composed image instead of original frame
    cv2.imshow('4 Blocks View', image)

    # Exit on pressing 'q'
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
