#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf

with tf.device('/cpu:0'):

    sess = tf.Session()

    # a_gpu = tf.Variable(0, name="a_gup")
    # sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True))

    hello = tf.constant('Hello, TensorFlow!')
    print(sess.run(hello))

    a = tf.constant(10)
    b = tf.constant(32)
    print(sess.run(a + b))

    c = tf.constant('haHa')
    print(sess.run(c))

    sess.close()
