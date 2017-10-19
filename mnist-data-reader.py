# decompresses and reads files byte by byte
# Author: Dillon Ward (Dillonward2017@gmail.com)
# Date: 16/10/2017

# import 'gzip' to open zipped files
import gzip
import numpy as np

# Part 1
def read_images(filename):
    with gzip.open(filename, 'rb') as f:
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

        # loop for the amount of images
        images = [[int.from_bytes(f.read(1), 'big') for i in range(rows * cols)] for j in range(10)]
        # print(images)
        return images

# output the third image in the traning set to the console
    # any pixel less than 128 is a '.', anything else is a '#'
# Author: Dillon Ward (Dillonward2017@gmail.com)
# Date: 18/10/2017

train_images = read_images('data/train-images-idx3-ubyte.gz')
# test_images = read_images('data/t10k-images-idx3-ubyte.gz')

for r in train_images:
    # if r % 28 == 0:
    #     print()

    if (train_images[r] <= 127):
        print('.', end='')
    else:
        print ('#', end='')