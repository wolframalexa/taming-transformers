from PIL import Image
import os

image_directory = "./images/"
x = 256
y = 256

#image = "./images/cmp_b0001.jpg"
for image in os.listdir(image_directory):
	try:
		path = image_directory + image
		original = Image.open(path)

		width, height = original.size   # Get dimensions
		left = (width - x)/2
		top = (height - y)/2
		right = (width + x)/2
		bottom = (height + y)/2
		cropped = original.crop((left, top, right, bottom))

		new_path = './cropped/' + image[:-4] + '_cropped.jpg'
		print(new_path)
		cropped.save(new_path, 'JPEG')
	except:
		print(image, "is not an image")
		pass
