from PIL import Image
import os

image_directory = "images"
x = 256
y = 256

image = "./images/cmp_b0001.jpg"
#for image in os.listdir(image_directory):
original = Image.open(image)

width, height = original.size   # Get dimensions
left = (width - x)/2
top = (height - y)/2
right = (width + x)/2
bottom = (height + y)/2
cropped_example = original.crop((left, top, right, bottom))
cropped_example.show()

cropped_example.save('./images/cmp_b0001_cropped.jpg', 'JPEG')
