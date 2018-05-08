#!/usr/bin/env python
# coding=utf-8

import tensorflow as tf

with tf.Graph().as_default(), tf.Session() as session:
    c = tf.constant('Hello World')
    v = tf.Variable([1, 2])
    v = v.assign([3, 4])
    v2 = tf.reshape(v, [1, 2])
    v3 = tf.reshape(v, [2, 1])

    session.run(tf.global_variables_initializer())
    print('result=%s' % session.run(c))
    print('v = %s shape=%s' % (v.eval(), v.get_shape()))
    print('v2 = %s v3 = \n %s' % (v2.eval(), v3.eval()))
