import numpy as np
import argparse
import cv2
from colors import *

def find_horizon(image):

	height, width = image.shape[:2]

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	blurred = cv2.GaussianBlur(gray, (11, 11), 0)

	avg_brightness = cv2.mean(blurred)[0]
	thresh = cv2.threshold(blurred, avg_brightness, 255, cv2.THRESH_BINARY)[1]
	print avg_brightness,

	if avg_brightness > 120:
		get_lines = thresh
	else:
		get_lines = blurred

	(mu, sigma) = cv2.meanStdDev(get_lines)
	edges = cv2.Canny(get_lines, mu - sigma, mu + sigma, apertureSize = 3)

	vy, vx, cy, cx = cv2.fitLine(np.argwhere(edges == 255), cv2.DIST_WELSCH, 0, 0.01, 0.01)

	if not np.isnan(vy):
		p1 = (int(cx-vx*width), int(cy-vy*width))
		p2 = (int(cx+vx*width), int(cy+vy*width))

		cv2.line(image, p1, p2, blue, 2)

	return image
