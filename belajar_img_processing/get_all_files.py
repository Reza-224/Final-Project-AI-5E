import cv2
import numpy as np
import glob

imdir = 'Dataset/Kemangi/'
ext = ['png', 'jpg', 'gif']    # Add image formats here\n",

files = []
[files.extend(glob.glob(imdir + '*.' + e)) for e in ext]

images = [cv2.imread(file) for file in files]
# adjust contrast to all of them nd save to different location
i = 1
for img in images:
    im_resized = cv2.resize(img, (400, 400))
    im_adjusted = cv2.addWeighted(im_resized, 1.5, np.zeros(im_resized.shape, im_resized.dtype), 0, -200)
    im_adjusted = cv2.addWeighted(img, 1.5, np.zeros(img.shape, img.dtype), 0, -100)
    im_name = "Dataset/anjust kemangi/" + str(i) + ".jpg"
    cv2.imwrite(im_name, im_adjusted)
    i+=1