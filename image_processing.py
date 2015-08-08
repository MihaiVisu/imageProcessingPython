import cv2
import sys
import os


class FaceRecognition(object):

	def __init__(self, imagePath, cascadePath, scaleFactor, minNeighbors, minSize, flags):
		self.imagePath = imagePath
		self.cascadePath = cascadePath
		self.scaleFactor = scaleFactor
		self.minNeighbors = minNeighbors
		self.minSize = minSize
		self.flags = flags

	def createCascade(self):
		return cv2.CascadeClassifier(self.cascadePath)

	def readImage(self):
		return cv2.imread(self.imagePath)

	def convertToGrayScale(self):
		return cv2.cvtColor(self.readImage(), cv2.COLOR_BGR2GRAY)

	def getFaces(self):
		return self.createCascade().detectMultiScale(
			self.convertToGrayScale(),
			scaleFactor=self.scaleFactor,
			minNeighbors=self.minNeighbors,
			minSize=self.minSize,
			flags=self.flags,
		)

	def drawFaceRectangles(self, color, borderWidth):
		faces = self.getFaces()
		image = self.readImage()
		for (x, y, w, h) in faces:
			cv2.rectangle(image, (x, y), (x+w, y+h), color, borderWidth)
		cv2.imshow("Resulted image", image)
		cv2.waitKey(0)
