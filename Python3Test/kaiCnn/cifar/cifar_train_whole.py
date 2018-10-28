#!/usr/bin/env python3
# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

batch_size = 128
output_every = 50
generations = 20000
eval_every = 500
image_height = 32
image_width = 32
crop_height = 24
crop_width = 24
num_channel = 3
num_target = 10

learning_rate = 0.1
lr_decay = 0.9
num_gens_to_wait = 250

image_vec_length = image_height * image_width * num_channel
record_length = 1 + image_vec_length


def read_cifar_files(filename_queue, distort_images=True):
    reader = tf.FixedLengthRecordReader(record_bytes=record_length)
    key, record_string = reader.read(filename_queue)
