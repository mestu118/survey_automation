from PIL import Image

from resizeimage import resizeimage
import os 
import sys

def resize(image_file, height, width):
    with open(image_file, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_cover(image, [height, width])
            cover.save(image_file, image.format)


def resize_all_images(height = 400, width = 340):
    for f in os.listdir('Images'):
        images = os.listdir('Images/' + f)
        for image in images:
            if image == '.DS_Store':
                continue
            image_dir = 'Images/' + f + '/' + str(image)
            resize(image_dir, height, width)

resize_all_images()

if __name__ == '__main__':
    print(len(sys.argv))
    if len(sys.argv) == 3:
        height = int(sys.argv[1])
        width = int(sys.argb[2])
        resize_all_images(height, width)
    else:
        resize_all_images(height, width)
