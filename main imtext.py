import urllib

from PIL import image
import pytesseract
from resizeimage import resizeimage
import os
import cv2
import numpy as np
src_path = "C:/Users/harindra sai tej/Desktop/Python/"
img_path = "C:/Users/harindra sai tej/Desktop/Python/"

def get_string(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2, COLOR_BGR2GRAY) # for convering Color image to gray
    kernel = np.ones((1,1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    # for removal of noise
    img = cv2.erode(img, kernel, iterations=1)
    # cv2.imwrite(src_path + "removed_noise.png", img)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imwrite(src_path + "thres.png", img)
    result = pytesseract.image_to_string(image.open(src_path + "thres.png"))

    return

print 'Start recognition\n'
print get_string(src_path + "street1.png")
