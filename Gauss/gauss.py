import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C:\\Users\\ankas\\OneDrive\\Desktop\\lena.png')

blur = cv2.GaussianBlur(img,(3,3),0)
blur2=cv2.GaussianBlur(img,(5,5),0)
blur3=cv2.GaussianBlur(img,(7,7),0)
plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(blur),plt.title('Gauss 3x3')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(blur2),plt.title('Gauss 5x5')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(blur3),plt.title('Gauss ')
plt.xticks([]), plt.yticks([])
plt.show()

