#!/usr/bin/env python3
# coding=utf-8

from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
from sklearn import datasets, svm

mnist = input_data.read_data_sets("../cache/mnist/", one_hot=True, source_url="http://yann.lecun.com/exdb/mnist/")

print(len(mnist.train.images))

print(len(mnist.test.images))

print(len(mnist.validation.images))

print(mnist.train.labels[1, :])

digits = datasets.load_digits()


def show_image(image, label):
    plt.figure(1, figsize=(3, 3))
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title(label)
    plt.show()


# show_image(digits.images[5], digits.target[5])


imageIndex = 1
singleImageLong = mnist.test.images[imageIndex]
singleImageSquare = singleImageLong.reshape(28, -1)

labelLong = mnist.test.labels[imageIndex]
labelStr = 'unknown'
for i in range(len(labelLong)):
    if labelLong[i] > 0.999:
        labelStr = i

show_image(singleImageSquare, labelStr)
