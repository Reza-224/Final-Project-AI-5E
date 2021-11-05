import cv2

img = cv2.imread('Daun Kemangi/001.jpg')
r = 400/img.shape[1]
dim = (400,int(img.shape[0]*r))
im_resized = cv2.resize(img, dim)
cv2.imshow('im_resized',im_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()