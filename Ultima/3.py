#detecteaza forme si culorile ish

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:\\Users\\ankas\\OneDrive\\Desktop\\shape.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.resize(img, (700, 600))

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_green = np.array([50, 100, 100])
upper_green = np.array([70, 255, 255])
mask_green= cv2.inRange(hsv, lower_green, upper_green)
green = cv2.bitwise_and(image, image, mask=mask_green)
#repara albastru
lower_blue = np.array([94, 80, 2]) 
upper_blue = np.array([126, 255, 255]) 
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
blue = cv2.bitwise_and(image, image, mask=mask_blue)
# imi face rosul-albastru

low_red = np.array([0,50,50])
high_red = np.array([10,255,255])
mask_red = cv2.inRange(hsv, low_red, high_red)
red = cv2.bitwise_and(image, image, mask=mask_red)

i = 0
for contour in contours:
	if i == 0:
		i = 1
		continue
	approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
	cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)

	M = cv2.moments(contour)
	if M['m00']!= 0.0:
		x = int(M['m10']/M['m00'])
		y = int(M['m01']/M['m00']) 
 
	if len(approx) == 3:
		cv2.putText(img, 'Triangle', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
		(x, y, w, h) = cv2.boundingRect(approx)
		ar = (w * float(h))/2
		print(ar)
	elif len(approx) == 4:
		cv2.putText(img, 'rectangle', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
		(x, y, w, h) = cv2.boundingRect(approx)
		ar = w * float(h)
		print(ar)
	else:
		cv2.putText(img, 'circle', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
		(x, y, w, h) = cv2.boundingRect(approx)
		r=float(h)/2
		pi=3.14
		ar = pi *r*r 
		print(ar)

plt.subplot(231),plt.imshow(image),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(green),plt.title('Verde')
plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(red),plt.title('Rosu')
plt.xticks([]), plt.yticks([])
plt.subplot(234),plt.imshow(blue),plt.title('Albastru')
plt.xticks([]), plt.yticks([])
plt.subplot(235),plt.imshow(img),plt.title('Shape')
plt.xticks([]), plt.yticks([])
plt.show()
