#I want to take in an image and allow the user to choose from multiple options such as
#transpose, grayscale, compress, extract, maybe more

import argparse
from PIL import Image
import sys
import image_processing

def initParser():
    parser = argparse.ArgumentParser(description='tool used for basic image processing')
    parser.add_argument('inputf', type=str, help="input file path")
    parser.add_argument('outputf', type=str, help="output file name, save over input file")
    parser.add_argument('-vt', '--verticalTranspose', action='store_true', help="flip the image vertically")
    parser.add_argument('-ht', '--horizontalTranspose', action='store_true', help="flip the image horizontally")
    parser.add_argument('-c', '--cut', nargs='*', type=int, help="Cut the image into smaller pieces. If no values are given, make the image into a 2x2 square. If one value (N) is given, make it onto a NxN square, If two values (N, M) are given, make it into a NxM quad.")
    parser.add_argument('-gs', '--grayscale', action='store_true', help="make the image grayscale")
    return parser.parse_args()

def main():
    args = initParser()
    try:
        img = Image.open(args.inputf)
    except IOError:
        sys.exit("Error: file %s not found in current directory" % args.inputf)
    if args.verticalTranspose:
        img = img.transpose(Image.FLIP_TOP_BOTTOM) 
    if args.horizontalTranspose:
        img = img.transpose(Image.FLIP_LEFT_RIGHT) 
    if args.grayscale:
        img = image_processing.img_to_grayscale(img)
    if args.cut != None:
        image_processing.cut_image(img, args.cut, args.outputf.split(".")[0])
    else:
        img.save(args.outputf)

if __name__ == '__main__':
    main()
