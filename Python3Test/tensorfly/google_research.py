#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf

with tf.Graph().as_default(), tf.Session() as sess:
    a = tf.constant([5, 3, 2, 7, 1, 4])
    b = tf.constant([4, 6, 3])
    print('a = \n%s' % a.eval())
    print('b = \n%s' % b.eval())
    reshaped_a = tf.reshape(a, [2, 3])
    reshaped_b = tf.reshape(b, [3, 1])
    print('ra = \n%s' % reshaped_a.eval())
    print('rb = \n%s' % reshaped_b.eval())
    c = tf.matmul(reshaped_a, reshaped_b)
    print('c = \n%s' % c.eval())

with tf.Graph().as_default(), tf.Session() as sess:
    dice1 = tf.Variable(tf.random_uniform([10, 1],
                                          minval=1, maxval=7,
                                          dtype=tf.int32))
    dice2 = tf.Variable(tf.random_uniform([10, 1],
                                          minval=1, maxval=7,
                                          dtype=tf.int32))

    dice_sum = tf.add(dice1, dice2)

    resulting_matrix = tf.concat(
        values=[dice1, dice2, dice_sum], axis=1)

    sess.run(tf.global_variables_initializer())

    print('result = \n%s' % resulting_matrix.eval())
