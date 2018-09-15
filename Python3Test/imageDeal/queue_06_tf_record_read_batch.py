#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf
import os

print(os.listdir('../cache/imageDeal/'))

files = tf.train.match_filenames_once('../cache/imageDeal/data.tfrecords-*')
filename_queue = tf.train.string_input_producer(files, shuffle=True, num_epochs=8)

reader = tf.TFRecordReader()
_, serialized_example = reader.read(filename_queue)
features = tf.parse_single_example(serialized_example, features={
    'i': tf.FixedLenFeature([], tf.int64),
    'j': tf.FixedLenFeature([], tf.int64),
})

example, label = features['i'], features['j']
batch_size = 3
capacity = 1000 + 3 * batch_size
# example_batch, label_batch = tf.train.batch([example, label], batch_size=batch_size, capacity=capacity)
example_batch, label_batch = tf.train.shuffle_batch([example, label], batch_size=batch_size, capacity=capacity, min_after_dequeue=1000)

with tf.Session() as sess:
    sess.run((tf.global_variables_initializer(), tf.local_variables_initializer()))
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    for i in range(10):
        cur_example_batch, cur_label_batch = sess.run([example_batch, label_batch])
        print(f'cur_example_batch={cur_example_batch}, cur_label_batch={cur_label_batch}')
    coord.request_stop()
    coord.join(threads)
