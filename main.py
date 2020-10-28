#I want to take in an image and allow the user to choose from multiple options such as
#transpose, grayscale, compress, extract, maybe more

import argparse
from PIL import Image
import numpy as np
import sys
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='herp derp description')
parser.add_argument('inputf', type=str, help="input file path")
parser.add_argument('outputf', type=str, help="output file name")
parser.add_argument('-gs', '--grayscale', action='store_true', help="make the image grayscale")
parser.add_argument('-vt', '--verticalTranspose', action='store_true', help="flip the image vertically")
parser.add_argument('-ht', '--horizontalTranspose', action='store_true', help="flip the image horizontally")
args = parser.parse_args()

def img_to_grayscale(img):
    arr = np.array(img.convert('L'))
    width, height = img.size
    fig = plt.figure(frameon=False, figsize=(width / 100, height / 100))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    plt.gray()
    plt.imshow(arr)

def save_img(img):
    if args.grayscale:
        plt.savefig(args.outputf)
    else:
        img.save(args.outputf)

def main():
    try:
        img = Image.open(args.inputf)
    except IOError:
        sys.exit("Error: file %s not found in current directory" % args.inputf)
    # do some img processing before creating a new output image
    if args.verticalTranspose:
        img = img.transpose(Image.FLIP_TOP_BOTTOM) 
    if args.horizontalTranspose:
        img = img.transpose(Image.FLIP_LEFT_RIGHT) 
    if args.grayscale:
        img_to_grayscale(img)
    save_img(img)

if __name__ == '__main__':
    main()
