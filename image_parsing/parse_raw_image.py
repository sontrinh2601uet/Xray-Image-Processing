# Created by Trinh Quang. Son
# Project: VietBa_IT_Image_Processing
# Date: 02-Apr-21
# Class: parse_raw_image.py
import os

import PIL
import PIL.ImageOps
from PIL import Image


class RawImageParser(object):

    def __init__(self, path_file, width, height, rotate=180):
        self.path_file = path_file
        self.width = width
        self.height = height
        self.rotate = rotate
        self.result_folder = r'.\result\output.png'

    def parse_raw_to_image(self):
        if not os.path.exists(os.path.dirname(self.result_folder)):
            os.mkdir(os.path.join(os.path.dirname(self.result_folder)))

        # image = np.fromfile(self.path_file, dtype='int16', sep="")
        # image = image.reshape([self.height, self.width])
        # plt.imshow(image)
        # plt.imsave(self.result_folder, image)

        raw_data = open(self.path_file, 'rb').read()
        img_size = (self.width, self.height)
        img = Image.frombuffer("L", img_size, raw_data, "raw", "I;16", 0, -1)
        img.save(self.result_folder)

    def start_image_processing(self):
        image = PIL.Image.open(self.result_folder)
        gray_image = PIL.ImageOps.grayscale(image)
        gray_image = PIL.ImageOps.equalize(gray_image)
        gray_image = PIL.ImageOps.invert(gray_image)
        gray_image.save(self.result_folder)

    def get_destination(self):
        target_image = PIL.Image.open(r".\data\destination.jpg")
        target_image = PIL.ImageOps.grayscale(target_image)
        target_image.save(r'.\result\destination.jpg')
