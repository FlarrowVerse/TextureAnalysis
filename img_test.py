import numpy as np
import cv2

img = cv2.imread("Wallpapers/codes-1.jpeg")
cv2.imshow("Image", img)
cv2.waitKey(0)

cv2.imwrite("Outputs/codes-1.jpeg", img)
