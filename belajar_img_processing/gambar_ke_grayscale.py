import cv2

img = cv2.imread('Daun Kemangi/001.jpg')
im_resized = cv2.resize(img, (400,400))
im_gray = cv2.cvtColor(im_resized, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original Image',im_resized)
cv2.imshow('Grayscale Image',im_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()