from PIL import Image

from resizeimage import resizeimage
import os 

def resize(image_file):
    with open(image_file, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [200, 140])
            cover.save(image_file, image.format)


def resize_all_images():
    for f in os.listdir('Images'):
        images = os.listdir('Images/' + f)
        for image in images:
            if image == '.DS_Store':
                continue
            image_dir = 'Images/' + f + '/' + str(image)
            resize(image_dir)

resize_all_images()