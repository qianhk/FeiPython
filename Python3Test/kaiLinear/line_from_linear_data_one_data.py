#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf
import numpy as np
import kaiLinear.line_from_linear_data_utils as kai

x_data_array, y_data_array = kai.get_linear_data()

w = tf.Variable(0, dtype=tf.float32, name='w')
b = tf.constant(50, dtype=tf.float32, name='b')

x_data = tf.placeholder(dtype=tf.float32, name='inputX')
y_target = tf.placeholder(dtype=tf.float32, name='yTarget')

y_calc = tf.add(tf.multiply(x_data, w), b, name='yCalc')

loss = tf.square(y_calc - y_target)
optimizer = tf.train.GradientDescentOptimizer(0.00001)
train = optimizer.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

loss_vec = []

data_amount = len(x_data_array)

for step in range(201):
    rand_index = np.random.choice(data_amount)
    x = x_data_array[rand_index]
    y = y_data_array[rand_index]
    sess.run(train, feed_dict={x_data: x, y_target: y})
    loss_value = sess.run(loss, feed_dict={x_data: x, y_target: y})
    loss_vec.append(loss_value)
    if step % 20 == 0:
        print('step=%d weight=%f bias=%f loss=%s' % (step, sess.run(w), sess.run(b), loss_value))

_w = sess.run(w)
_b = sess.run(b)

sess.close()

print('last W=%f B=%f' % (_w, _b))

kai.show_visualization_data(x_data_array, y_data_array, _w, _b, loss_vec, title='One Data')
