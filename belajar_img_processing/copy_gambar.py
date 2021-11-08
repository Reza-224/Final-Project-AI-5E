import cv2
#copy gambar
img = cv2.imread('Daun Kemangi/001.jpg')

cp_image = img.copy()
print(cp_image.shape)