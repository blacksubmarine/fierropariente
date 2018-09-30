import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('midbrainDegraded.png')
#img = np.float32(img)
blur = cv2.blur(img,(10,10))

laplacian = cv2.Laplacian(blur,cv2.CV_64F)
#
sobelx = cv2.Sobel(blur,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(blur,cv2.CV_64F,0,1,ksize=5)
sobel = sobelx+sobely

canny = cv2.Canny(blur, 30, 100)

plt.imshow(canny,)

plt.figure(1)
plt.subplot(231),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])

plt.subplot(233),plt.imshow(laplacian),plt.title('Laplaciano')
plt.xticks([]), plt.yticks([])

plt.subplot(234,),plt.imshow(canny,cmap = 'gray'),plt.title('canny')
plt.xticks([]), plt.yticks([])
plt.show()

