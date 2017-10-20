# (1) Adapted from https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist
# (2) Adapted from https://stackoverflow.com/questions/902761/saving-a-numpy-array-as-an-image
# decompresses and reads files byte by byte
# Author: Dillon Ward (Dillonward2017@gmail.com)
# Date: 16/10/2017

# import 'gzip' to open zipped files 
import gzip
# import numpy for using lists
import numpy as np
# import PIL.Image to save images to a file
import PIL.Image as pil 
# import os to see if path exists and create one
import os

train_imgs_dir = 'data/train-images-idx3-ubyte.gz'
test_imgs_dir = 'data/t10k-labels-idx1-ubyte.gz'

# Part 1
def read_images(file):
    with gzip.open(file, 'rb') as f:
        # reads in the first byte which is the magic number
            # prints out the magic number - new way of formatting
        magic = int.from_bytes(f.read(4), 'big')
        print("The Magic number is: {:>6}".format(magic))

        # reads in the next byte which is the number of images
        imgs = int.from_bytes(f.read(4), 'big')
        print('Number of images: {:>10}'.format(imgs))

        # reads in the number of rows and columns
        rows, cols = int.from_bytes(f.read(4), 'big'), int.from_bytes(f.read(4), 'big')
        print('Rows:{:>20}'.format(rows))
        print('Cols: {:>19}'.format(cols))
        print()
        # loop for and read in all the bytes for the length of rows * columns
        # only loops through the first 11 images because range is set to 10
        # if you want to loop through all of the images, change '10' to 'imgs'
        images = [[int.from_bytes(f.read(1), 'big') for i in range(rows * cols)] for j in range(11)]
        return images

# output the third image in the traning set to the console
    # any pixel less than 128 is a '.', anything else is a '#'
# Author: Dillon Ward (Dillonward2017@gmail.com)
# Date: 18/10/2017

# Part 2
def image_to_console(file):
    # selects the 3 image from the file
    for j in range(len(file[2])):
        # use a counter, if the counter is divisable by 28 (the length of a row)
            # print out a new line
        if j % 28 == 0:
            print()

            # if the byte being read in is less than or equal to 127
            # print '.'
        if (file[2][j] <= 127):
            print('.', end='')

        # otherwise, print '#'    
        else:
            print ('#', end='')
    print()

# output the files as PNGs and save them
# Author: Dillon Ward (Dillonward2017@gmail.com)
# Date: 20/10/2017

# Part 3
def read_labels(file):
    with gzip.open(file, 'rb') as f:
        # reads in the magic number
        magic = int.from_bytes(f.read(4), 'big')
        # reads in the number of labels as 'imgs'
        imgs = int.from_bytes(f.read(4), 'big')

        # populate a list of labels for the amount of imgs
        labels = [f.read(1) for i in range(imgs)]
        # convert the bytes to ints
        labels = [int.from_bytes(label, 'big') for label in labels]
        return labels


def save_image(image, name, num, label):

    # save the file as a png from an array - ref: (2)
    image_name = 'images/%s-%05d-%d.png'
    img = pil.fromarray(image).convert('RGB')
    img.save(image_name %(name, num, label))
    return


train_labels = read_labels(train_imgs_dir)
# test_labels = read_labels(test_imgs_dir)

train_images = read_images(train_imgs_dir)
# test_images = read_images(test_imgs_dir)

image_to_console(train_images)

# checks if the directory 'images' exists locally - if it doesn't, create it - ref: (1)
if not os.path.exists('images'):
    os.makedirs('images')


# loop for the amount of train images
for i in range(len(train_images)):
    # parameters being sent to the 'save_image' function are being passed from an array
    # continuously make new images for the amount of images/labels read in
    save_image(train_images[i], 'train', (i+1), train_labels[i]) # image format