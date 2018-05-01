#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

mock_data = np.genfromtxt('../data/linear_data.csv', delimiter=',', skip_header=1, dtype=float)
# print('mock_data=\n%s' % mock_data)

x_data_array = np.array(mock_data[:, 0])
y_data_array = np.array(mock_data[:, 1])
print('x_data=\n%s' % x_data_array)
print('y_data=\n%s' % y_data_array)

w = tf.Variable(0, dtype=tf.float32, name='w')
# w = tf.Variable(tf.random_normal(shape=[1]), dtype=tf.float32, name='w')

# b = tf.Variable(0, dtype=tf.float32, name='b')
# b = tf.Variable(tf.zeros([1]), dtype=tf.float32, name='b')
# b = tf.Variable(0., name='b')
b = tf.constant(50, dtype=tf.float32, name='b')

y_array = w * x_data_array + b

loss = tf.reduce_mean(tf.square(y_array - y_data_array))
optimizer = tf.train.GradientDescentOptimizer(0.0001)
train = optimizer.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

loss_vec = []

for step in range(201):
    sess.run(train)
    loss_vec.append(sess.run(loss))
    if step % 20 == 0:
        print('step=%d weight=%f bias=%f loss=%s' % (step, sess.run(w), sess.run(b), sess.run(loss)))

_w = sess.run(w)
_b = sess.run(b)

sess.close()

print('last W=%f B=%f' % (_w, _b))

best_fit = []
for x in x_data_array:
    best_fit.append(_w * x + _b)

fig = plt.figure()
plt.title('Use All Data')

ax = fig.add_subplot(121)
ax.scatter(x_data_array, y_data_array, color='y', label="样本", linewidths=0.5)
ax.plot(x_data_array, best_fit, color='b', linewidth=2)

ax = fig.add_subplot(122)
ax.plot(loss_vec, color='g', linewidth=1)
plt.show()
