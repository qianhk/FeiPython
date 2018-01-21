#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf

matrix1 = tf.constant([[3., 3.]])

matrix2 = tf.constant([[2.], [2.]])

product = tf.matmul(matrix1, matrix2)

sess = tf.Session()

result = sess.run(product)
print(result)

sess.close()

tf.reset_default_graph()

state = tf.Variable(0, name="counter")

one = tf.constant(1)
other = tf.placeholder(tf.int32)
new_value = tf.add(tf.add(state, one), other)
update = tf.assign(state, new_value)

init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    with tf.device("/gpu:1"):
        sess.run(init_op)
        print(sess.run([state, new_value], feed_dict={other: 1}))
        for _ in range(5):
            sess.run(update, feed_dict={other: 2})
            print(sess.run([state, new_value], feed_dict={other: 3}))
