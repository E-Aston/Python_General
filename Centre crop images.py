def crop(file):
    from PIL import Image
    im = Image.open(file)

# Choose image size. For the D850, starting image size is 8256 x 5504, aspect ratio 1.5. Cropping down to 24MP
# preserves this aspect ratio and shrinks the file size down massively.

    new_width = 6000
    new_height = 4000

    width, height = im.size   # Get dimensions
    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2

    # Crop the center of the image
    im = im.crop((left, top, right, bottom))

    im.save(file)

import os

directory = "C:/Insert/Directory/Here"  # Sets WD where obj files are stored - INPUT NEEDED
for filename in os.listdir(directory):
    if filename.endswith(".JPG"):
        crop(os.path.join(directory, filename))
    else:
        continue