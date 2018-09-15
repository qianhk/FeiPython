#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf
import os

print(os.listdir('../cache/imageDeal/'))

files = tf.train.match_filenames_once('../cache/imageDeal/data.tfrecords-*')
filename_queue = tf.train.string_input_producer(files, shuffle=False, num_epochs=10)

reader = tf.TFRecordReader()
_, serialized_example = reader.read(filename_queue)
features = tf.parse_single_example(serialized_example, features={
    'i': tf.FixedLenFeature([], tf.int64),
    'j': tf.FixedLenFeature([], tf.int64),
})

with tf.Session() as sess:
    sess.run((tf.global_variables_initializer(), tf.local_variables_initializer()))
    print(f'files={sess.run(files)}')

    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    for i in range(6):
        f_i, f_j = sess.run([tf.cast(features['i'], tf.int32), features['j']])
        print(f"idx={i} i={f_i} j={f_j}")

    coord.request_stop()
    coord.join(threads)
