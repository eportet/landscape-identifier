import numpy as np
import argparse
import cv2
import glob

from colors import *
from light import find_light_source
from horizon import find_horizon
from daytime import find_daytime

images = [[cv2.imread(file), file] for file in glob.glob("img/*.png")]

font                   = cv2.FONT_HERSHEY_PLAIN
fontScale              = 1
lineType               = 1

time = 'Time: '

for image in images:

	img = image[0]
	name = image[1]
	print(name + ":"),

	out = img
	out, roi = find_light_source(img)
	out = find_horizon(img)
	daytime = time + find_daytime(img, roi)
	print '.'

	alpha = 0.5
	overlay = out.copy()
	cv2.rectangle(overlay, (5, 130), (180, 200), black, -1)
	cv2.addWeighted(overlay, alpha, out, 1 - alpha, 0, out)
	cv2.putText(out, 'O Light Source', (10, 150), font, fontScale, yellow, lineType)
	cv2.putText(out, '- Horizon', (10, 170), font, fontScale, blue, lineType)
	cv2.putText(out, daytime, (10, 190), font, fontScale, white, lineType)


	cv2.imshow("Images", out)

	if cv2.waitKey(0) == ord('n'):
		continue
	elif cv2.waitKey(0) == ord('q'):
		break;
