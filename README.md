## Image Manipulation CLI

CLI written in Python that allows a user to alter images

### main functions: <br />
**1** - Add a given image (like a logo) to the bottom right of all images within a given directory <br />
takes up to 4 arguments <br/>
call it like: `python main.py -bl <image_folder> <logo> <output_folder> .5` <br/>
`-bl` indicates that we want to use the bulk logo add functionality <br/>
`<image_folder>` is the path to the folder of images that you want to add the logo to <br/>
`<logo>` is the path to the image file used as the logo <br/>
`<output_folder>` (optional) is where the new files with the logo added will be saved, defaults to "./output_folder" <br/>
`.5` (optional) indicates the maximum ratio of the original image that one of the dimensions of the logo will take up
<img src="./example_images/doge.jpg" width="400">
<img src="./example_images/sky.png" width="400">

**2** - Cut image into squares for use in giga emojis on slack and discord <br/>
call it like: `python main.py -if <input_image_file> -of <output_file> -c 2 3` <br/>
`-if` indicates that we want to alter/manipulate a single image <br/>
`<input_image_file>` is the path to the input image <br/>
`-of` (optional) indicates that we want to supply a base file name to save the image(s) to <br/>
`<output_file>` is a path to the output file(s) <br/>
`-c` indicates that we want to cut this image into squares <br/>
`2` (optional) indicates that we want to cut the image into 2 equal columns, if ommitted will result in cutting into 2x2 grid <br/>
`3` (optional) indicates that we want to cut the image into 3 equal rows, if ommitted will rely on the first number for both the columns and rows <br/>
if the image aspect ratio doesn't match the ratio of the given dimensions, a prompt will indicate this and ask if you'd like to proceed anyways <br/>
eg. we can turn a beloved meme: <br/>
<img src="./example_images/big-chungus.png" width="100"> <br/>
into a large emoji in slack: <br/>
<img src="./example_images/big emoji.PNG" width="200"> <br/>
there are also tags such as `-vt` and `-ht` that vertically and horizontally transpose the image, respectively, and `-gs` which turns the image to grayscale <br/>
a list and explanation of all the tags and arguments can be seen by running `python main.py -h` to see the help text
