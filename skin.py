import cv2
import numpy as np


# create webcam window
web_alt = "Changed"
cv2.namedWindow(web_alt)
web_ori = "Original"
cv2.namedWindow(web_ori)

camera = cv2.VideoCapture(0)


# skin color range 
# https://ieeexplore.ieee.org/document/7005726
min = np.array([0, 51, 40])
max = np.array([17, 153, 255])

while True:
    # read the camera
    _ ,frame = camera.read()
    
    # convert BGR -> HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # pixels no intervalo [min, max] = 255, out of range = 0
    mask = cv2.inRange(hsv_frame, min, max)
    
    # apply the mask
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    # show image
    cv2.imshow(web_ori, frame)
    cv2.imshow(web_alt, result)


    # stop when pressing a key
    if cv2.waitKey(1) != -1:
        break
    

camera.release()
cv2.destroyAllWindows()