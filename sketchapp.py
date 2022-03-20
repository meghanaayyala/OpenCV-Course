#installing and importing necessary packages

pip install numpy
pip install opencv-python
import cv2
import numpy as np


def sketch(image): #function defined taking input as image 

# convert the captured image into gray scale image
# A normal image consists of 3 layers Red,Blue,Green and thus forms a 3 dimensional matrix, whereas gray scale image is a 2 dimensional matrix.
# We compress the image to grayscale
    grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# blurring the image
# It blurs the gray scale image obtained through the above operation. It is useful for removing noise. 
# It actually removes high frequency content (eg: noise, edges) from the image.
# We simply reduce the edge content and makes the transition form one color to the other very smooth.

    blurimg = cv2.GaussianBlur(grayimg, (3, 3), 0)

# extracting edges
# First argument is our input image. Second and third arguments are our minVal and maxVal respectively.

    edges = cv2.Canny(blurimg, 10, 80)

# applying threshold
    # :Gray scale image is converted into Binary Image, it uses a threshold.
    # Thresholding is a process of converting image to binary form.In OpenCV thresholding is done on grayscale images, which have pixel values ranging from 0–255.
    # Suppose gray scale values are from 0 (Pure Black) to 255(Pure White), 
    # values greater than threshold will be converted into 1 (White) and below to threshold will be converted into 0 (Black).
    ret, mimg = cv2.threshold(edges, 50, 255, cv2.THRESH_BINARY_INV)
    #ret is a boolean variable that returns true if the frame is available.
    return mimg


# Capturing video from webcam

vid_capt = cv2.VideoCapture(0)
#VideoCapture is a function to open the Webcam and capture the video

# Capturing the video frame by frame

while True:
    ret, pic_capt = vid_capt.read() #It captures the video frame by frame.
    cv2.imshow('Sketch App', sketch(pic_capt)) #For each image captured it calls the function sketch as defined above, and also opens a dialog box with sketch of images

   # Key13 is ENTER_KEY
   # function terminates and the dialog box closes after pressing the enter button
    if cv2.waitKey(1) == 13:
        break

# releasing_webcam

vid_capt.release()

# destroying_window

cv2.destroyAllWindows()
