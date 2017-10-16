# reads data from files byte by byte
# Author: Dillon Ward (Dillonward2017@gmail.com)
# Date: 16/10/2017

# import 'gzip' to open zipped files
import gzip
import numpy as np

def read_images(filename):
    with gzip.open(filename, 'rb') as f:
        magic = int.from_bytes(f.read(4), 'big')
        # prints out the magic number - new way of formatting
        print("The Magic number is: {:>6}".format(magic))

        imgs = int.from_bytes(f.read(4), 'big')
        print('Number of images: {:>10}'.format(imgs))

        rows, cols = int.from_bytes(f.read(4), 'big'), int.from_bytes(f.read(4), 'big')
        print('Rows:{:>20}'.format(rows))
        print('Cols: {:>19}'.format(cols))

        images = []

train_images = read_images('data/train-images-idx3-ubyte.gz')