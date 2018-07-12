import numpy as np
import cv2

def find_scene(image):
	# labels_file = 'caffe_ilsvrc12/synset_words.txt'
	# labels = np.loadtxt(labels_file, str, delimiter='\t')

	labels_file = 'mit_scene/IndoorOutdoor_places205.csv'
	labels = np.loadtxt(labels_file, str, delimiter='\n')

	# net = cv2.dnn.readNetFromCaffe('deploy.prototxt.txt', 'bvlc_reference_caffenet.caffemodel')
	net = cv2.dnn.readNetFromCaffe('mit_scene/deploy.prototxt.txt', 'mit_scene/8conv3fc_DSN.caffemodel')

	blob = cv2.dnn.blobFromImage(cv2.resize(image, (227, 227)))
	print("[INFO] computing object detections...")
	net.setInput(blob)
	detections = net.forward()

	top = detections[0].argsort()[::-1][:8]

	labels = labels[top]

	return ', '.join(labels)

# image = cv2.imread('img/image1.png')
# print find_scene(image)
