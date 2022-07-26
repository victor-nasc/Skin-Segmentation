# Skin-Segmentation
Skin Segmentation using Numpy and OpenCV 


### Digital image processing for human skin segmentation
The color pattern of the image is converted from BGR to HSV and then each pixel is compared to human skin color range values to decide whether that pixel is skin or not, depending on whether the value of that pixel is in the range of human skin color. 

skin.py uses your webcam to apply the filter


Human skin color range  :
  
    0  <= H <= 17
    51 <= S <= 153 
    40 <= V <= 255 
    https://ieeexplore.ieee.org/document/7005726
        
        
       
### Results
