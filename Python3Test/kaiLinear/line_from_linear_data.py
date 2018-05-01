#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

mock_data = np.genfromtxt('../data/linear_data.csv', delimiter=',', skip_header=1, dtype=float)
# print('mock_data=\n%s' % mock_data)

x_data = np.array(mock_data[:, 0])
y_data = np.array(mock_data[:, 1])
print('x_data=\n%s' % x_data)
print('y_data=\n%s' % y_data)

w = tf.Variable(0, dtype=tf.float32, name='w')
# w = tf.Variable(tf.random_normal(shape=[1]), dtype=tf.float32, name='w')

# b = tf.Variable(0, dtype=tf.float32, name='b')
# b = tf.Variable(tf.zeros([1]), dtype=tf.float32, name='b')
# b = tf.Variable(0., name='b')
b = tf.constant(50, dtype=tf.float32, name='b')

y = w * x_data + b

loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.0001)
train = optimizer.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

loss_vec = []

for step in range(201):
    sess.run(train)
    loss_vec.append(sess.run(loss))
    if step % 20 == 0:
        print('step=%d weight=%f bias=%f' % (step, sess.run(w), sess.run(b)))

W = sess.run(w)
B = sess.run(b)

sess.close()

print('last W=%f B=%f' % (W, B))

best_fit = []
for x in x_data:
    best_fit.append(W * x + B)

fig = plt.figure()

ax = fig.add_subplot(121)
ax.scatter(x_data, y_data, color='y', label="样本", linewidths=0.5)
ax.plot(x_data, best_fit, color='b', linewidth=2)

ax = fig.add_subplot(122)
ax.plot(loss_vec, color='g', linewidth=1)
plt.show()
