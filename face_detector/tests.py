
import cv2
import requests

from django.test import TestCase


class ImageTestCase(TestCase):
    def get_data(self):
        # define the URL to our face detection API
        url = "http://localhost:8000/face_detection/detect/"

        image = cv2.imread("obama.jpg")
        payload = {"url": "http://www.pyimagesearch.com/wp-content/uploads/2015/05/obama.jpg"}
        r = requests.post(url, data=payload).json()
        print "obama.jpg: {}".format(r)
        self.assertNotEqual(r['num_faces'], 0)
        print "Found {} faces.".format(r['num_faces'])

        # loop over the faces and draw them on the image
        for (startX, startY, endX, endY) in r["faces"]:
            cv2.rectangle(image, (startX, startY), (endX, endY), (255, 255, 0), 1)
        print "Drawn rectangles."
