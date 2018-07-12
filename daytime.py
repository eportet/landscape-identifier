import numpy as np
import argparse
import cv2
from colors import *

def find_daytime(image, roi):

	image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

	outcomes = ['Daytime', 'Dusk', 'Night']

	if roi != None:
		mask = np.zeros(image.shape[:2], dtype=np.uint8)
		cv2.circle(mask, roi[0], roi[1], white, -1)
		mean = cv2.mean(image, mask)
	else:
		mean = cv2.mean(image)

	# Convert to traditional HSV ranges
	h = int(mean[0]*2)
	s = int(((mean[1]+1)/256)*100)
	v = int(((mean[2]+1)/256)*100)
	mean = [h, s, v]

	print mean,

	if mean[2] < 10:
		return outcomes[2]
	elif ((0 <= mean[0] and mean[0] <= 85) or (190 <= mean[0] and mean[0] <= 195)) and mean[1] > 15:
		return outcomes[1]

	return outcomes[0]
