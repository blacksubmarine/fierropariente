import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
img = cv.imread('midbrainDegraded.png',0)
#filtramos la imagen de ruido
img = cv.blur(img,(10,10))
print( img.shape)


ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)#este es el que interesa
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()



print( images[1].shape)
plt.hist(images[1].ravel(),120,[0,120]); plt.show()

edges = cv.Canny(images[1],100,200)
cv.imshow('Edges',edges)

if cv.waitKey(0) & 0xff == 27:#esta con q se acaba el programa
    cv.destroyAllWindows()