#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf

# input1 = tf.constant([1.0, 2.0, 3.0], name = 'N_input1')
# input2 = tf.Variable(tf.random_uniform([3]), name = 'N_input2')
# output = tf.add_n([input1, input2], name = 'Nadd')
#
# writer = tf.summary.FileWriter("./logs/boardTest", tf.get_default_graph())
# writer.close()


a = tf.constant(5, name="input_a")
b = tf.constant(3, name="input_b")
c = tf.multiply(a, b, name="mul_c")
d = tf.add(a, b, name="add_d")
e = tf.add(c, d, name="add_e")

sess = tf.Session()
print(sess.run(e))
output = sess.run(e)

writer = tf.summary.FileWriter('./logs/boardTest', graph=sess.graph)
writer.close()
print(sess.run(e))
