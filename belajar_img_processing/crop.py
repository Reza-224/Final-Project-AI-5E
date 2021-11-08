import cv2
#crop gambar
img = cv2.imread('Daun Kemangi/001.jpg')
im_crop = img[100:600, 100:380]

cv2.imshow('crop',im_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(im_crop.shape)