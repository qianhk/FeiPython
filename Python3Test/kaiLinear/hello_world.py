#!/usr/bin/env python
# coding=utf-8

import tensorflow as tf

c = tf.constant('Hello World')
c2 = tf.constant(123)

session = tf.Session()
print(session.run(c))
print(session.run(c2))

session.close()
