#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# z = 2x + y - 1

x_data_array = np.array([0, 0, 1, 1, 2, 2])
y_data_array = np.array([1, 2, 1, 2, 1, 2])
target_data_array = np.array([0, 1, 2, 3, 4, 5])
# print('x_data=\n%s' % x_data_array)
# print('y_data=\n%s' % y_data_array)

w1 = tf.Variable(0, dtype=tf.float32, name='w1')
w2 = tf.Variable(0, dtype=tf.float32, name='w2')

b = tf.Variable(0., name='b')
# b = tf.constant(0., name='b')

z_array = w1 * x_data_array + w2 * y_data_array + b

loss = tf.reduce_mean(tf.square(target_data_array - z_array))
optimizer = tf.train.GradientDescentOptimizer(0.0003)
train = optimizer.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

loss_vec = []

for step in range(10_0001):
    sess.run(train)
    loss_vec.append(sess.run(loss))
    if step % 100 == 0:
        print('step=%d w1=%f w2=%f bias=%f loss=%s' % (step, sess.run(w1), sess.run(w2), sess.run(b), sess.run(loss)))

_w1 = sess.run(w1)
_w2 = sess.run(w2)
_b = sess.run(b)

sess.close()

print('last W1=%f W2=%f B=%f' % (_w1, _w2, _b))

best_fit = []
for idx in range(len(x_data_array)):
    best_fit.append(_w1 * x_data_array[idx] + _w2 * y_data_array[idx] + _b)

print('best_fit=\n%s' % best_fit)
