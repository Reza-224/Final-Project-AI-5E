import cv2
import numpy as np
img = cv2.imread('Daun Kemangi/001.jpg')

im_resized = cv2.resize(img, (400,400))
im_adjusted = cv2.addWeighted(im_resized, 1.5, np.zeros(im_resized.shape, im_resized.dtype), 0, -200)
cv2.imshow('Original Image',im_resized)
cv2.imshow('Adjusted Image',im_adjusted)
cv2.waitKey(0)
cv2.destroyAllWindows()