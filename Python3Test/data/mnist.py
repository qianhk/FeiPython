#!/usr/bin/env python3
# coding=utf-8

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("../cache/mnist/", one_hot=True, source_url="http://yann.lecun.com/exdb/mnist/")

print(len(mnist.train.images))

print(len(mnist.test.images))

print(len(mnist.validation.images))

print(mnist.train.labels[1, :])




