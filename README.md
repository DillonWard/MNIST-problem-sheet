## MNIST Problem Sheet
###### *Dillon Ward - G00326756 - Emerging Technologies*
---
## Introduction
The following repository contains solutions to MNIST problem sheets written in Python for the module Emerging Technologies. The module is taught to undergraduate students at GMIT in the Department of Computer Science and Applied Physics. The lecturer is Ian McLoughlin.

## Prerequisites
* [git](https://git-scm.com/)
* [Python](https://www.python.org/downloads/)

## Cloning this Repository
To clone this repository and run the solutions, do the following:

```
In the command line change to a directory:
cd <directory>

Clone the repository:
git clone https://github.com/DillonWard/MNIST-problem-sheet.git

Change directory into the cloned folder:
cd <folder name>

*To ensure you're in the right folder, you can run the ls command to display all the files inside the folder. 
Files ending with 'py' are Python files.*
   
   
Run the program:
py <program name>.py
```

## MNIST
### What is MNIST?
The MNIST database (Modified National Institute of Standards and Technology database) is a large database of handwritten digits that is commonly used for training various image processing systems, and is widely used in the field of machine learning. The MNIST database contains 60,000 traning images and 10,000 test images. Each image in the dataset is 28 by 28 pixels and can be interpreted as a big 2D array of numbers.


![Matrix](https://github.com/DillonWard/MNIST-problem-sheet/blob/master/images/MNIST-Matrix.png) 


<a href="https://emerging-technologies.github.io/problems/mnist.html" target="_blank">Worksheet</a>
----

##### *The following list contains problems and the solution to the worksheet. Raw code can be found by following the solution listed below.*
### Read the Data Files
Download the image and label files. Have Python decompress and read them byte by byte into appropriate data structures in memory.

### Output an image to the console
Output the third image in the training set to the console. Do this by representing any pixel value less than 128 as a full stop and any other pixel value as a hash symbol.

### Output the image files as PNGs
Use Python to output the image files as PNGs, saving them in a subfolder in your repository. Name the images in the format `train-XXXXX-Y.png` or `test-XXXXX-Y.png` where `XXXXX` is the image number (where it occurs in the data file) and `Y` is its label. For instance, the five-thousandth training image is labelled 2, so its file name should be `train-04999-2.png`. Note the images are indexed from 0, so the five-thousandth image is indexed as 4999. See below for an example of it. Commit these image files to GitHub.


## <a href="https://raw.githubusercontent.com/DillonWard/MNIST-problem-sheet/master/mnist-data-reader.py" target="_blank">Solution</a>

## References
[Wikipedia](https://en.wikipedia.org/wiki/MNIST_database)

[TensorFlow](https://www.tensorflow.org/get_started/mnist/beginners)