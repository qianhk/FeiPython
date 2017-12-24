#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf

# with tf.name_scope('S_input1'):
#     input1 = tf.constant([1.0, 2.0, 3.0], name = 'N_input1')
#
# with tf.name_scope("S_input2"):
#     input2 = tf.Variable(tf.random_uniform([3]), name = 'N_input2')
#
# output = tf.add_n([input1, input2], name = 'Nadd')
#
# writer = tf.summary.FileWriter("./logs/boardTest", tf.get_default_graph())
# writer.close()


# a = tf.constant(5, name="input_a")
# b = tf.constant(3, name="input_b")
# c = tf.multiply(a, b, name="mul_c")
# d = tf.add(a, b, name="add_d")
# e = tf.add(c, d, name="add_e")
#
# sess = tf.Session()
# print(sess.run(e))
# output = sess.run(e)
#
# writer = tf.summary.FileWriter('./logs/boardTest', graph=sess.graph)
# writer.close()
# print(sess.run(e))


# with tf.variable_scope("foo"):
#     a = tf.get_variable("bar", [1])
#     print(a.name)
#
# with tf.variable_scope("bar"):
#     b = tf.get_variable("bar", [1])
#     print(b.name)
#
# with tf.name_scope('a'):
#     a = tf.Variable([1])
#     print(a.name)
#
#     a = tf.get_variable("b", [1])
#     print(a.name)
#
# with tf.name_scope('b'):
#     try:
#         b = tf.get_variable("b", [1])
#         print('again: ' + b.name)
#     except ValueError as err:  # ValueError: Variable b already exists
#         print('found exception: ')
#     else:
#         print('no exception')



