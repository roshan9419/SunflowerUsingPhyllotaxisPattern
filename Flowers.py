import cv2
import numpy as np
import math

x_axis = 600
y_axis = 600
window = np.zeros((y_axis, x_axis, 3), np.uint8)

cv2.putText(window, "Press any Key", (50,300),cv2.FONT_ITALIC, 2, (255,255,255), 3)
cv2.imshow("Sunflower",window)
cv2.waitKey()
window[:] = 0,0,0
n = 0
c = 4
radius = 4
B = 255
G = 255
R = 255
Angle = 137.5

while (n<3500):
	if(n<100):
		B,G,R = 19,54,134
		radius = 4
	elif(n<500):
		B,G,R = 9,32,64 
		Angle = 137.5
	elif(n<1000):
		B,G,R = 15,140,203 
		Angle = 200.5
		radius = 3
	elif(n<1500):
		B,G,R = 22,168,211 
		Angle = -137.5
		radius = 4
	elif(n<2000):
		B,G,R = 57,218,250
		Angle = 200.5
		radius = 3
	elif(n<2500):
		Angle = -137.3
		radius = 4
	elif(n<3000):
		Angle = 200.5
		radius = 2
	a = n * Angle
	r = c * math.sqrt(n)
	x = int(r * math.cos(a) + x_axis/2)
	y = int(r * math.sin(a) + y_axis/2)
	cv2.circle(window, (x, y), radius, (B,G,R))
	n += 1
	cv2.imshow("Sunflower", window)
	key = cv2.waitKey(1)
	if key==ord('q'):
		break

cv2.circle(window, (x, y), radius, (B,G,R))
cv2.waitKey(0)
