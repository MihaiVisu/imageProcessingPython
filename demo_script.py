
import cv2
import os
from image_processing import FaceRecognition

abs_root = '/Users/mihaivisuian/Documents/Projects/opencv_face_recognition_python'
image_path = abs_root+'/Demo Pictures/abba.png'
cascade_path = abs_root+'/Cascade Files/haarcascade_frontalface_default.xml'

im_processing = FaceRecognition(
	image_path, 
	cascade_path,
	1.1,
	5,
	(30, 30),
	cv2.cv.CV_HAAR_SCALE_IMAGE,
)

im_processing.drawFaceRectangles((0,255,255), 1)
