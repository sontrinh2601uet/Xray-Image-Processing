# Created by Trinh Quang. Son
# Project: VietBa_IT_Image_Processing
# Date: 02-Apr-21
# Class: parse_raw_image.py
import os

import PIL
import PIL.ImageOps
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageEnhance


class RawImageParser(object):

    def __init__(self, path_file, width, height, rotate=180):
        self.path_file = path_file
        self.width = width
        self.height = height
        self.rotate = rotate
        self.result_folder = r'.\result\output.jpg'

    def parse_raw_to_image(self):
        if not os.path.exists(os.path.dirname(self.result_folder)):
            os.mkdir(os.path.join(os.path.dirname(self.result_folder)))

        image = np.fromfile(self.path_file, dtype='int16', sep="")
        image = image.reshape([self.height, self.width])
        plt.imshow(image)
        plt.imsave(self.result_folder, image)

    def start_image_processing(self):
        image = Image.open(self.result_folder)
        raw_image = image.rotate(self.rotate)
        raw_image.save(self.result_folder)

        image = PIL.Image.open(self.result_folder)
        gray_image = PIL.ImageOps.grayscale(image)
        gray_image = PIL.ImageOps.equalize(gray_image)
        gray_image.save(self.result_folder)

        # img = Image.open(self.result_folder)  # get image
        # pixels = img.load() # create the pixel map
        #
        # for i in range(img.size[0]):  # for every pixel:
        #     for j in range(img.size[1]):
        #         if pixels[i, j] > 100:
        #             pixels[i, j] = 170
        #
        # img.save(self.result_folder)

    def get_destination(self):
        target_image = PIL.Image.open(r".\data\destination.jpg")
        target_image = PIL.ImageOps.grayscale(target_image)
        target_image = PIL.ImageOps.invert(target_image)
        target_image.save(r'.\result\destination.jpg')
