#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf
import numpy as np

sess = tf.Session()

x_vals = np.array([1., 3, 5, 7, 9])
x_data = tf.placeholder(tf.float32)
m = tf.constant(3.)

prod = tf.multiply(x_data, m)

for x_val in x_vals:
    print(sess.run(prod, feed_dict={x_data: x_val}))

sess.close()

merged = tf.summary.merge_all()

my_writer = tf.summary.FileWriter('../logs/boardTest', sess.graph)
my_writer.close()
