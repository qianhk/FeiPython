#!/usr/bin/env python3
# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np
import os
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

cache_dir = '../../cache/'
extract_folder = os.path.join(cache_dir, 'cifar-10-batches-bin')


def read_cifar_files(filename_queue, distort_images=True):
    reader = tf.FixedLengthRecordReader(record_bytes=record_length)
    key, record_string = reader.read(filename_queue)
    record_bytes = tf.decode_raw(record_string, tf.uint8)
    image_label = tf.cast(tf.slice(record_bytes, [0], [1]), tf.int32)
    image_extracted = tf.reshape(tf.slice(record_bytes, [1], [image_vec_length]), [num_channel, image_height, image_width])
    image_uint8image = tf.transpose(image_extracted, [1, 2, 0])
    reshaped_image = tf.cast(image_uint8image, tf.float32)
    final_image = tf.image.resize_image_with_crop_or_pad(reshaped_image, crop_width, crop_height)
    if distort_images:
        final_image = tf.image.random_flip_left_right(final_image)
        final_image = tf.image.random_brightness(final_image, max_delta=63)
        final_image = tf.image.random_contrast(final_image, lower=0.2, upper=1.8)
    final_image = tf.image.per_image_standardization(final_image)
    return final_image, image_label


def input_pipeline(batch_size, train_logical=True):
    if train_logical:
        files = [os.path.join(extract_folder, f'data_batch_{i}.bin') for i in range(1, 6)]
    else:
        files = [os.path.join(extract_folder, 'test_batch.bin')]
    filename_queue = tf.train.string_input_producer(files)
    image, label = read_cifar_files(filename_queue)
    min_after_dequeue = 1000
    capacity = min_after_dequeue + 3 * batch_size
    example_batch, label_batch = tf.train.shuffle_batch([image, label], batch_size, capacity, min_after_dequeue)
    return example_batch, label_batch
