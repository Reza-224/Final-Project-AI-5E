import cv2
#mengubah nilai pixel
img = cv2.imread('Daun Kemangi/001.jpg')

img[300:350, 170:300] = (200, 100, 20)
cv2.imshow('cp_image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()