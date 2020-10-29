from PIL import Image
import numpy as np
import sys
import matplotlib.pyplot as plt
import io

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
    if len(dimensions) > 2:
        sys.exit('Too mamy args given with "cut" flag')
    if len(dimensions) == 0:
        rows = columns = 2
    if len(dimensions) == 1:
        rows = columns = dimensions[0]
    else:
        columns = dimensions[0]
        rows = dimensions[1]
    width, height = img.size
    print(width, height, columns, rows)
    if width/height != columns/rows:
        print("Height and width of input image are not equal so the resulting cut images won't fit well together in a giga emoji.")
        print("Continue anyway? y/n")
        inp = input()
        if ['y', 'Y'].count(inp) != 1:
            sys.exit()
    for y in range(rows):
        for x in range(columns):
            tempImg = img.crop((x * (width/columns), y * (height/rows), (x+1) * (width/columns), (y+1) * (height/rows)))
            tempImg.save(outputFile + "_" + str(x) + "_" + str(y) + ".png")
