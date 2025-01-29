# importing PIL.Image library and os library

from PIL import Image  # from PIL import Image
import os

# Deletes old created images if they exist
images = [
    "combinedFilters.jpg",
    "filter1.jpg",
    "filter2.jpg",
    "filter3.jpg",
    "grey.jpg",
]

# had to add path, change to "" for repl
pictureDir = "/Users/james/dev/python/learningPython/images/"
# List Comprehensions
images = [pictureDir + image for image in images]
# Remove old images
# Map
list(map(lambda fn: os.remove(fn) if os.path.exists(fn) else None, images))

# Adds two blank lines before any output
print("\n\n")

# Opens image - upload a Local File into repl.it
img = Image.open(pictureDir + "image.jpg")

# Rescale image size down, if original is too large
width = img.width
height = img.height
mwidth = width // 1000
mheight = height // 1000
if mwidth > mheight:
    scale = mwidth
else:
    scale = mheight
if scale != 0:
    img = img.resize((width // scale, height // scale))


def filterGreyLogic(p):
    r = p[0]
    g = p[1]
    b = p[2]
    # Perform pixel manipulation and stores results
    # to a new red, green and blue components
    newr = (r + g + b) // 3
    newg = (r + g + b) // 3
    newb = (r + g + b) // 3
    return newr, newg, newb


def grey():
    return dynamicFilter(filterGreyLogic)


# was filter1()
# returns r,g,b
def filter1Logic(pixel):
    return 0, pixel[1], 0


def dynamicFilter(rgbModFunc):
    print("Code for dynamicFilter")
    # Creates an ImageCore Object from original image
    pixels = img.getdata()
    # Creates empty array to hold new pixel values
    new_pixels = []
    # For every pixel from our original image, it saves
    # a copy of that pixel to our new_pixels array
    for p in pixels:
        new_pixels.append(p)
    # Starts at the first pixel in the image
    location = 0
    # Continues until it has looped through all pixels
    while location < len(new_pixels):
        # Gets the current color of the pixel at location
        p = new_pixels[location]
        newr, newg, newb = rgbModFunc(p)
        # Assign new red, green and blue components to pixel
        # at that specific location
        new_pixels[location] = (newr, newg, newb)
        # Changes the location to the next pixel in array
        location = location + 1
    # Creates a new image, the same size as the original
    # using RGB value format
    newImage = Image.new("RGB", img.size)
    # Assigns the new pixel values to newImage
    newImage.putdata(new_pixels)
    # Sends the newImage back to the main portion of program
    return newImage


def filter1():
    print("Code for filter1")
    return dynamicFilter(filter1Logic)


#####################################
#    Your Filters with User Input   #
#####################################


# was filter1()
# returns r,g,b
def filter2Logic(p):
    r = p[0]
    g = p[1]
    b = p[2]
    # Perform pixel manipulation and stores results
    # to a new red, green and blue components
    newr = (r + g) // 2
    newg = (g + b) // 6
    newb = (r + b) // 3
    return newr, newg, newb


def filter2():
    print("Code for filter2")
    return dynamicFilter(filter2Logic)


def saveImage(file, name):
    file.save(pictureDir + name)


def filter3Logic(p):
    r = p[0]
    g = p[1]
    b = p[2]
    # Perform pixel manipulation and stores results
    # to a new red, green and blue components
    newr = (g * b) // 2
    newg = (r * g) // 5
    newb = (r * b) // 10
    return newr, newg, newb


def filter3():
    print("Code for filter3")
    return dynamicFilter(filter3Logic)


# Creates the four filter images and saves them to our files
a = grey()
saveImage(a, "grey.jpg")
b = filter1()
saveImage(b, "filter1.jpg")
c = filter2()
saveImage(c, "filter2.jpg")
d = filter3()
saveImage(d, "filter3.jpg")

# Image filter names for use below
f1 = "filter1"
f2 = "filter2"
f3 = "filter3"

# Apply multiple filters through prompts with the user
answer = input(
    "\nWhich filter do you want me to apply?\n grey\n "
    + f1
    + "\n "
    + f2
    + "\n "
    + f3
    + "\n none\n\n"
)
while (
    answer != "grey"
    and answer != f1
    and answer != f2
    and answer != f3
    and answer != "none"
):
    answer = input(
        "\nIncorrect filter, please enter:\n grey\n "
        + f1
        + "\n "
        + f2
        + "\n "
        + f3
        + "\n none\n\n"
    )

while answer == "grey" or answer == f1 or answer == f2 or answer == f3:
    if answer == "grey":
        img = grey()
    elif answer == f1:
        img = filter1()
    elif answer == f2:
        img = filter2()
    elif answer == f3:
        img = filter3()
    else:
        break
    print('Filter "' + answer + '" applied...')
    answer = input(
        "\nWhich filter do you want me to apply next?\n grey\n "
        + f1
        + "\n "
        + f2
        + "\n "
        + f3
        + "\n none\n\n"
    )
    while (
        answer != "grey"
        and answer != f1
        and answer != f2
        and answer != f3
        and answer != "none"
    ):
        answer = input(
            "\nIncorrect filter, please enter:\n grey\n "
            + f1
            + "\n "
            + f2
            + "\n "
            + f3
            + "\n none\n\n"
        )
print("Image being created...Done")

# Create the combined filter image and saves it to our files
img.save(pictureDir + "combinedFilters.jpg")
