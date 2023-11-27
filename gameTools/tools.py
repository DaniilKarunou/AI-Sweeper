import os

import pygame
from PIL import Image

def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    resized_image = original_image.resize(size)
    try:
        os.mkdir("temporaryFiles/")
    except:
        pass
    resized_image.save(output_image_path)
    photo = pygame.image.load(output_image_path)
    return photo