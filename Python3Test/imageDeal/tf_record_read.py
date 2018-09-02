#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf
import os

reader = tf.TFRecordReader()

filename = '../logs/imageDeal/mnist_train.tfrecords'
if not os.path.exists(filename):
    print(f'File not exist: {filename}')
else:
    filename_queue = tf.train.string_input_producer([filename])
    _, serialized_example = reader.read(filename_queue)

    features = tf.parse_single_example(serialized_example, features={
        'image_raw': tf.FixedLenFeature([], tf.string),
        'pixels': tf.FixedLenFeature([], tf.int64),
        'label': tf.FixedLenFeature([], tf.int64),
    })

    features_image_raw = features['image_raw']
    images = tf.decode_raw(features_image_raw, tf.uint8)
    features_label = features['label']
    labels = tf.cast(features_label, tf.int32)
    features_pixels = features['pixels']
    pixels = tf.cast(features_pixels, tf.int32)

    sess = tf.Session()
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    for i in range(10):
        image, label, pixel = sess.run([images, labels, pixels])
        print(f'idx={i} label={label} pixel={pixel}')

    sess.close()
