#!/usr/bin/env python3
# coding=utf-8


import matplotlib.pyplot as plt
import os
import tensorflow as tf

image_height = 32
image_width = 32
num_channel = 3

batch_size = 128

image_vec_length = image_height * image_width * num_channel
record_length = 1 + image_vec_length

extract_folder = os.path.join('../../cache/', 'cifar-10-batches-bin')


def read_cifar_files(filename_queue):
    reader = tf.FixedLengthRecordReader(record_bytes=record_length)
    key, record_string = reader.read(filename_queue)
    record_bytes = tf.decode_raw(record_string, tf.uint8)
    image_label = tf.cast(tf.slice(record_bytes, [0], [1]), tf.int32)
    image_extracted = tf.reshape(tf.slice(record_bytes, [1], [image_vec_length]), [num_channel, image_height, image_width])
    image_uint8image = tf.transpose(image_extracted, [1, 2, 0])
    return image_uint8image, image_label


def input_pipeline(batch_size):
    files = [os.path.join(extract_folder, 'test_batch.bin')]
    filename_queue = tf.train.string_input_producer(files)
    image, label = read_cifar_files(filename_queue)
    min_after_dequeue = 1000
    capacity = min_after_dequeue + 3 * batch_size
    example_batch, label_batch = tf.train.shuffle_batch([image, label], batch_size, capacity, min_after_dequeue)
    return example_batch, label_batch


test_images, test_targets = input_pipeline(batch_size)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
tf.train.start_queue_runners(sess=sess)

Nrows = 8
Ncols = 8

# 经测试，发现figsize，1 代表100像素 (mbp 15寸)

plt.figure(figsize=(16, 16))

for i in range(Nrows * Ncols):
    ori_image = test_images[i]
    # 不转换也行, imShow支持浮点图片(0.0 ~ 1.0)和uint8图片(0-255)
    float_image = tf.image.convert_image_dtype(ori_image, dtype=tf.float32)
    image = sess.run(float_image)  # (32, 32, 3)
    label = sess.run(test_targets[i])  # (1,)

    # print(f'image={image} label={label}')

    plt.subplot(Nrows, Ncols, i + 1)
    plt.imshow(image)
    plt.title(f'no.{label}', fontsize=10)
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    frame.axes.get_yaxis().set_visible(False)

plt.show()
