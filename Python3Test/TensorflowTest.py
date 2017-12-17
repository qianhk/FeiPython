#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf

sess = tf.Session()

hello = tf.constant('Hello, TensorFlow!')
print(sess.run(hello))

a = tf.constant(10)
b = tf.constant(32)
print(sess.run(a + b))

c = tf.constant('haHa')
print(sess.run(c))

sess.close()
