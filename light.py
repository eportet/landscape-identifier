import numpy as np
import cv2
from colors import *


def find_light_source(image):

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (11, 11), 0)

	avg_brightness = cv2.mean(blurred)[0]
	(_, maxVal, _, maxLoc) = cv2.minMaxLoc(blurred)
	ratio = avg_brightness/maxVal

	thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]

	i = 1
	while True:
		i += 1
		thresh = cv2.erode(thresh, None, iterations=1)
		_, contours, hierarchy = cv2.findContours(thresh, 2, 1)
		if len(contours) <= 1:
			break


	roi = None

	if len(contours) < 1:
		if  draw_bright(avg_brightness, ratio):
			cv2.circle(image, maxLoc, 50, yellow, 2)
			roi = [maxLoc, 50]
	else:
		(x,y), radius = cv2.minEnclosingCircle(contours[0])
		center = (int(x),int(y))
		radius = int(radius*0.6)
		# print "r:", radius,

		# We have a good contour
		if radius < 180 and radius > 30:
			cv2.circle(image, center, radius, yellow, 2)
			roi = [center, radius]

		# We can pick a good bright spot
		elif draw_bright(avg_brightness, ratio):
			cv2.circle(image, maxLoc, 50, yellow, 2)
			roi = [maxLoc, 50]
		# Dont display a light source


	# print 'avg:', avg_brightness, 'max:', maxVal, 'ratio:', ratio,


	return image, roi

def draw_bright(avg, r):
	if  avg < 120 and r < 0.39:
		return True
	return False
