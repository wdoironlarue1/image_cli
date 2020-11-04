import os
import glob
from PIL import Image
import copy
import sys


def validate_args(args):
    if len(args) < 2:
        sys.exit("Need to include path to folder and path to logo file as first and second args, respectively")
    elif len(args) > 4:
        sys.exit("Too many arguments supplied. Possible arguments are: folder path, logo path, ouput path, and max logo ratio")
    elif not os.path.isdir(args[0]):
        sys.exit("couldn't find folder %s" % args[0])



def bulk_add_logo(args):
    validate_args(args)
    folderPath = args[0] + '/'
    logoPath = args[1]
    if len(args) > 2: outputPath = args[2] + '/'
    else: outputPath = './output_folder/'
    if len(args) > 3: maxLogoRatio = float(args[3]) 
    else: maxLogoRatio = .5
    try:
        logo = Image.open(logoPath)
    except IOError:
        sys.exit("Error: file %s not found" % logoPath)
    fileTypes = ('*.png', '*.jpg')
    images = []
    if not os.path.isdir(outputPath):
        os.mkdir(outputPath)
    for type in fileTypes:
        for file in glob.glob(folderPath + type):
            img = Image.open(file)
            img.filename = file
            images.append(img)
    for image in images:
        imageWidth, imageHeight = image.size
        tempLogo = copy.deepcopy(logo)
        logo.thumbnail((imageWidth * maxLogoRatio, imageHeight * maxLogoRatio), Image.ANTIALIAS)
        smallerLogo = logo
        logo = tempLogo
        slogoWidth, slogoHeight = smallerLogo.size
        image.paste(smallerLogo, (imageWidth - slogoWidth, imageHeight - slogoHeight, imageWidth, imageHeight), smallerLogo)
        image.save(outputPath + image.filename.split("\\")[-1])