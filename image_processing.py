from PIL import Image
import numpy as np
import sys
import matplotlib.pyplot as plt
import io
import os

def img_to_grayscale(img):
    arr = np.array(img.convert('L'))
    width, height = img.size
    fig = plt.figure(frameon=False, figsize=(width / 100, height / 100))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    plt.gray()
    plt.imshow(arr)
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    return Image.open(buf)

def cut_image(img, dimensions, outputFile):
    outputFile = os.path.splitext(outputFile)[0]
    if len(dimensions) > 2:
        sys.exit('Too mamy args given with "cut" flag')
    if len(dimensions) == 0:
        rows = columns = 2
    elif len(dimensions) == 1:
        rows = columns = dimensions[0]
    else:
        columns = dimensions[0]
        rows = dimensions[1]
    width, height = img.size
    if width/height != columns/rows:
        print("Ratio of the height and width of input image (%d, %d) not equal to ratio of desired rows and columns (%d, %d)." % (height, width, rows, columns))
        print("Continue anyway? y/n")
        inp = input()
        if ['y', 'Y'].count(inp) != 1:
            sys.exit()
    for y in range(rows):
        for x in range(columns):
            tempImg = img.crop((x * (width/columns), y * (height/rows), (x+1) * (width/columns), (y+1) * (height/rows)))
            tempImg.save(outputFile + "_" + str(x) + "_" + str(y) + ".png")

def open_img_file(inputf):
    try:
        return Image.open(inputf)
    except IOError:
        sys.exit("Error: file %s not found" % inputf)
