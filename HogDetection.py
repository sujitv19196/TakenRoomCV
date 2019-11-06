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

    boxes, weights = hog.detectMultiScale(image, winStride=(4,4), padding=(8,8), scale=1.05)
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
    for (xA, yA, xB, yB) in boxes:
        # display the detected boxes in the colour pictures
        cv2.rectangle(frame, (xA, yA), (xB, yB),
                        (0, 255, 0), 2)
    boxes = np.array([[x, y, x+w, y+h] for (x,y,w,h) in boxes])
    pick = non_max_suppression(boxes, probs=None, overlapThresh=0.65)

    for (xA, yA, xB, yB) in pick:
        cv2.rectangle(frame, (xA, yA), (xB, yB),
                        (0, 255, 0), 2)
    
    if (len(pick) > 0):
        #send to updater 

    # Display the resulting frame
    cv2.imshow('image',image)
        
    # When everything done, release the capture
    cap.release()

    # finally, close the window
    cv2.destroyAllWindows()
    cv2.waitKey(1)

