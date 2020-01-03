import numpy as np
import cv2

black = np.zeros([150, 200, 1], 'uint8')
cv2.imshow("Black", black)
print(black[0,0,:])

ones = np.ones([150,200,3], 'uint8')
cv2.imshow("Ones", ones)
print(black[0,0,:])

colored = np.ones([150,200,3], 'uint16')
colored *= 255;
cv2.imshow("Color", colored)
print(colored[0,0,:])

cv2.waitKey(0)
cv2.destroyAllWindows()
