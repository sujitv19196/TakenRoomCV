# import the necessary packages
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2

def detect(path):
	# initialize the HOG descriptor/person detector
	hog = cv2.HOGDescriptor()
	hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
	cv2.startWindowThread()

	image = cv2.imread(path)

	image = imutils.resize(image, width=min(400, image.shape[1]))

	# detect people in the image
	(rects, weights) = hog.detectMultiScale(image, winStride=(2, 2),
		padding=(8, 8), scale=1.05)
 
	# apply non-maxima suppression to the bounding boxes using a
	# fairly large overlap threshold to try to maintain overlapping
	# boxes that are still people
	rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
	pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
 
	# draw the final bounding boxes
	for (xA, yA, xB, yB) in pick:
		cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

	# if (len(pick) > 0):
	# 	#send to updater 

	cv2.imshow('image', image)
	cv2.waitKey(0)

