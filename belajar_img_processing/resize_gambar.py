import cv2
#meresize gambar
img = cv2.imread('Daun Kemangi/001.jpg')
im_resized = cv2.resize(img, (400,400))
cv2.imshow('im_resized',im_resized)

cv2.waitKey(0)
cv2.destroyAllWindows()