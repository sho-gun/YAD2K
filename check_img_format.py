import argparse
import os

import numpy as np
from PIL import Image, ImageDraw, ImageFont

parser = argparse.ArgumentParser(
    description='')
parser.add_argument(
    'image_path',
    help='path to target image file')

def _main(args):
    image_path = os.path.expanduser(args.image_path)

    img = np.array(Image.open(image_path))
    print(img.shape)
    if img.shape[2] == 4:
        img = img[:, :, :3]
        img = Image.fromarray(img)
        # img.show()
        img.save('output_' + image_path)

if __name__ == '__main__':
    _main(parser.parse_args())
