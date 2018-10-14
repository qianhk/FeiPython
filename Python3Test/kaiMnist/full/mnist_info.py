#!/usr/bin/env python3
# coding=utf-8

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('../../cache/mnist/', one_hot=True)
train = mnist.train
print(f'Train data size: {train.num_examples}')
print(f'Validation data size: {mnist.validation.num_examples}')
print(f'Test data size: {mnist.test.num_examples}')

item = train.images[0]
print(f'Example training data: {item.shape}')

label = train.labels[0]
print(f'Example training data label: {label} {label.shape}')

batch_size = 8
xs, ys = mnist.train.next_batch(batch_size=batch_size)
print(f'X shape: {xs.shape} Y shape: {ys.shape}')
