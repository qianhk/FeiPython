#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf
import numpy as np
from tensorflow.python.framework import ops

ops.reset_default_graph()

sess = tf.Session()

# 造数据 y=x+K (K=15)

# 数据数量
data_amount = 1001

x_vals = np.linspace(20, 100, data_amount)
# print(x_vals)

y_vals = np.add(x_vals, 15)
# print(y_vals)

y_offset_vals = np.random.normal(0, 0.5, data_amount)
# print(y_offset_vals)

y_vals = np.add(y_vals, y_offset_vals)
print(y_vals)


x_data = tf.placeholder(shape=[1], dtype=tf.float32)
y_target = tf.placeholder(shape=[1], dtype=tf.float32)

# 构造K
K = tf.Variable(tf.random_normal(mean=0, shape=[1]))

multiply = tf.add(x_data, K)
calcY = multiply

loss = tf.square(calcY - y_target)

# print(loss)

init = tf.global_variables_initializer()
sess.run(init)

print('init K=' + str(sess.run(K)))

my_opt = tf.train.GradientDescentOptimizer(0.02)
train_step = my_opt.minimize(loss)

for i in range(1000):
    rand_index = np.random.choice(data_amount)
    x = [x_vals[rand_index]]
    y = [y_vals[rand_index]]
    sess.run(train_step, feed_dict={x_data: x, y_target: y})
    if (i + 1) % 25 == 0:
        print('Step #' + str(i + 1) + ' K = ' + str(sess.run(K)))
        print('Loss = ' + str(sess.run(loss, feed_dict={x_data: x, y_target: y})))

# print('Last K = ' + str(sess.run(K)) + '  Loss = ' + str(sess.run(loss, feed_dict={x_data: 1000, y_target: 5003})))

print('\nOver\n')

sess.close()
