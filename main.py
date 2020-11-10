import argparse
from PIL import Image
import image_processing
import bulk_logo_add

def initParser(parser):
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-if', '--inputf', type=str, help="input file path")
    parser.add_argument('-of', '--outputf', type=str, help="output file path, overwrites input file if ommitted")
    parser.add_argument('-vt', '--verticalTranspose', action='store_true', help="flip the image vertically")
    parser.add_argument('-ht', '--horizontalTranspose', action='store_true', help="flip the image horizontally")
    parser.add_argument('-c', '--cut', nargs='*', type=int, help="Cut the image into smaller pieces. If no values are given, make the image into a 2x2 square. If one value (N) is given, make it onto a NxN square, If two values (N, M) are given, make it into a NxM quad.")
    parser.add_argument('-gs', '--grayscale', action='store_true', help="make the image grayscale")
    group.add_argument('-bl', '--bulkLogoAdd', nargs='*', help="Add a logo to all the images in a folder. First arg is the folder path, second arg is the logo file path, third arg is output folder path (will output to ./output/ if ommitted), fourth arg is the max ratio of the logo to the image that it's being placed on(.5 if ommitted).")
    return parser.parse_args()

def main():
    parser = argparse.ArgumentParser(description='tool used for basic image processing')
    args = initParser(parser)
    if args.inputf != None:
        outputf = args.outputf or args.inputf
        img = image_processing.open_img_file(args.inputf)
        if args.verticalTranspose:
            img = img.transpose(Image.FLIP_TOP_BOTTOM) 
        if args.horizontalTranspose:
            img = img.transpose(Image.FLIP_LEFT_RIGHT) 
        if args.grayscale:
            img = image_processing.img_to_grayscale(img)
        if args.cut != None:
            image_processing.cut_image(img, args.cut, outputf)
        else:
            img.save(outputf)
    elif args.bulkLogoAdd != None:
        bulk_logo_add.bulk_add_logo(args.bulkLogoAdd)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
