import cv2

img = cv2.imread('Daun Kemangi/001.jpg')
(h, w) = img.shape[:2]
center = (w/2, h/2)

M = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(img, M, (w,h))
cv2.imshow('rotate',rotated)
cv2.imwrite("rotate.png", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()