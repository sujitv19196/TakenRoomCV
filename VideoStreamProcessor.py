import numpy as np
import cv2
import time
import os

#the program will analyze a fram every kFrameAnalysisWindow seconds 
kFrameAnalysisWindow = 10

def startStream():
    stream = cv2.VideoCapture(0)
    start_time = time.time()
    i = 0
    while(True):
        elapsed_time = time.time() - start_time
        if (elapsed_time == kFrameAnalysisWindow):
            ret, frame = stream.read()
            cv2.imwrite('temp_image_storage/to_analyze{index}.png'.format(index=i), frame)
            start_time = time.time()
            i+=1    
            #HOG
            #UPDATE 
if __name__ == "__main__":
    startStream()
    
    
