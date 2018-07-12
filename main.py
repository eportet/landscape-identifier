import numpy as np
import argparse
import cv2
import glob

from colors import *
from light import find_light_source
from horizon import detect_horizon

images = [[cv2.imread(file), file] for file in glob.glob("img/*.png")]

font                   = cv2.FONT_HERSHEY_PLAIN
fontScale              = 1
lineType               = 1

for image in images:

	img = image[0]
	name = image[1]
	print(name + ":"),

	out = find_light_source(img)
	out = detect_horizon(img)
	print '.'

	alpha = 0.5
	overlay = out.copy()
	cv2.rectangle(overlay, (5, 130), (150, 180), black, -1)
	cv2.addWeighted(overlay, alpha, out, 1 - alpha, 0, out)
	cv2.putText(out, 'O Light Source', (10,150), font, fontScale, yellow, lineType)
	cv2.putText(out, '- Horizon', (10,170), font, fontScale, blue, lineType)


	cv2.imshow("Images", out)

	if cv2.waitKey(0) == ord('n'):
		continue
	elif cv2.waitKey(0) == ord('q'):
		break;
