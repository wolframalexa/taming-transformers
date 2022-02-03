from PIL import Image
import os
import random
import math

image_directory = "./images/"
x = 256
y = 256

# crop facades images to x and y coordinates above
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
		print(image, "is not an image") # don't crop .txt files
		pass


test = open('./text/facade_test.txt', 'w')
train = open('./text/facade_training.txt', 'w')

# use a 90-10 split, training-test
files = os.listdir('./cropped/')
numfiles = len(files)
print("The dataset has", numfiles, "files in it")

train_files = random.sample(files, math.floor(numfiles * 0.9)) # remaining files used for test
test_files = list(set(files) - set(train_files))

for item in train_files:
	line = './cropped/' + item + '\n'
	train.writelines(line)

print(len(train_files))
print(len(test_files))

for item in test_files:
	line = './cropped/' + item + '\n'
	test.writelines(line)

