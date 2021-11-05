import cv2
import numpy as np
img = cv2.imread('Daun Kemangi/001.jpg')

im_resized = cv2.resize(img, (400,400))
im_edges = cv2.Canny(im_resized, 100, 200)

cv2.imshow('Original Image',im_resized)
cv2.imshow('Detected Edges',im_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()