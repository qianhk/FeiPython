#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf
import numpy as np

sess = tf.Session()

my_array = np.array([[1, 3, 5, 7, 9], [-2, 0, 2, 4, 6], [-6, -3, 0, 3, 6]])

x_vals = np.array([my_array, my_array + 1], dtype=np.float32)
x_data = tf.placeholder(tf.float32, shape=(3, None), name="x_data")

m1 = tf.constant([[1.], [0], [-1], [2], [4]], name="m1")  #shape=(5, 1)
m2 = tf.constant([[2]], dtype=np.float32, name="m2")   #shape=(1,1)
a1 = tf.constant([[10]], dtype=np.float32, name="a1")    #shape=(1,1)

prod1 = tf.matmul(x_data, m1, name="prod1")   #shape=(3, 1)
prod2 = tf.matmul(prod1, m2, name="prod2")   #shape=(3, 1)
add1 = tf.add(prod2, a1, name="add1")    #shape=(3, 1)

for x_val in x_vals:
    # print(x_val)
    # print(sess.run(prod2, feed_dict={x_data: x_val}))
    print(sess.run(add1, feed_dict={x_data: x_val}))

sess.close()

writer = tf.summary.FileWriter('../logs/boardTest', graph=sess.graph)
writer.close()
