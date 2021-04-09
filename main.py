# Created by Trinh Quang. Son
# Project: VietBa_IT_Image_Processing
# Date: 02-Apr-21
# Class: main.py
from image_parsing.parse_raw_image import RawImageParser


if __name__ == '__main__':
    raw_data_path = r".\data\CHEST-PA.RAW"

    width = 2448
    height = 2984

    raw_image_parser = RawImageParser(
        path_file=raw_data_path,
        width=width,
        height=height
    )

    raw_image_parser.parse_raw_to_image()
    raw_image_parser.start_image_processing()

    raw_image_parser.get_destination()

