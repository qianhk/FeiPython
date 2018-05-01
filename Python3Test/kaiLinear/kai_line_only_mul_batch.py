#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf
import numpy as np
from tensorflow.python.framework import ops
import matplotlib.pyplot as plt

ops.reset_default_graph()

sess = tf.Session()

# 造数据 y=Kx+3 (K=5)

# 数据数量
data_amount = 101
batch_size = 50

x_vals = np.linspace(20, 200, data_amount)
# print(x_vals)

y_vals = np.multiply(x_vals, 5)
y_vals = np.add(y_vals, 3)
# print(y_vals)

y_offset_vals = np.random.normal(0, 15, data_amount)
# print(y_offset_vals)

y_vals = np.add(y_vals, y_offset_vals)
# print(y_vals)


x_data = tf.placeholder(shape=[None, 1], dtype=tf.float32)
y_target = tf.placeholder(shape=[None, 1], dtype=tf.float32)

# 构造K
K = tf.Variable(tf.random_normal(mean=0, shape=[1, 1]))

calcY = tf.add(tf.matmul(x_data, K), 3)

loss = tf.reduce_mean(tf.square(y_target - calcY))

# print(loss)

init = tf.global_variables_initializer()
sess.run(init)

print('init K=' + str(sess.run(K)))

my_opt = tf.train.GradientDescentOptimizer(0.0000005)
train_step = my_opt.minimize(loss)

loss_vec = []

for i in range(1000):
    rand_index = np.random.choice(data_amount, size=batch_size)
    x = np.transpose([x_vals[rand_index]])
    y = np.transpose([y_vals[rand_index]])
    sess.run(train_step, feed_dict={x_data: x, y_target: y})

    tmp_loss = sess.run(loss, feed_dict={x_data: x, y_target: y})
    loss_vec.append(tmp_loss)

    if (i + 1) % 25 == 0:
        print('Step #' + str(i + 1) + ' K = ' + str(sess.run(K)))
        print('Loss = ' + str(sess.run(loss, feed_dict={x_data: x, y_target: y})))

rand_index = np.random.choice(data_amount, size=batch_size)
x = np.transpose([x_vals[rand_index]])
y = np.transpose([y_vals[rand_index]])

print('\nLast K = ' + str(sess.run(K)) + '  Loss = ' + str(sess.run(loss, feed_dict={x_data: x, y_target: y})))

print('\nOver\n')

[[KValue]] = sess.run(K)

print(KValue)

sess.close()

best_fit = []
for i in x_vals:
    best_fit.append(KValue * i + 3)

# plt.plot(x_vals, y_vals, 'o', label='Data')
# plt.plot(x_vals, best_fit, 'r-', label='Base fit line')
plt.plot(loss_vec, 'k-')

# yticks = np.linspace(0, 5000, 11)
# plt.yticks(yticks)
plt.title('Batch Look Loss')
plt.xlabel('Generation')
plt.ylabel('Loss')
plt.show()
