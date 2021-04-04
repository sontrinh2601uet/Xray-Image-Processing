# Created by Trinh Quang. Son
# Project: VietBa_IT_Image_Processing
# Date: 02-Apr-21
# Class: parse_raw_image.py
import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


class RawImageParser(object):

    def __init__(self, path_file, width, height, rotate=180):
        self.path_file = path_file
        self.width = width
        self.height = height
        self.rotate = rotate
        self.result_folder = r'.\result\output.jpg'

    def parse_raw_to_image(self):
        if not os.path.exists(os.path.dirname(self.result_folder)):
            os.mkdir(os.path.dirname(os.path.dirname(self.result_folder)))

        image = np.fromfile(self.path_file, dtype='int16', sep="")
        image = image.reshape([self.height, self.width])
        plt.imshow(image)
        plt.imsave(self.result_folder, image)

    def start_image_processing(self):
        image = Image.open(self.result_folder)

        image = image.rotate(self.rotate)
        image = self._shift_hue(image, 10)

        image.save(self.result_folder)

    def _shift_hue(self, image, shift, ):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)

        shift_h = (h + shift) % 180
        shift_hsv = cv2.merge([shift_h, s, v])
        shift_img = cv2.cvtColor(shift_hsv, cv2.COLOR_HSV2BGR)

        return shift_img

