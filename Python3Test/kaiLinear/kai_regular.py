#!/usr/bin/env python
# coding=utf-8

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

n = 14
pie_size = np.arange(1, n + 1, 1)
pie_price = np.log(pie_size) * 10 + 2
# pie_price += np.random.normal(0, 1.5, [n])

b = tf.Variable(0, dtype=tf.float32)
w1 = tf.Variable(0, dtype=tf.float32)
w2 = tf.Variable(0, dtype=tf.float32)
w3 = tf.Variable(0, dtype=tf.float32)
w4 = tf.Variable(0, dtype=tf.float32)

method = 1

y_array = w1 * pie_size + b

loss = tf.reduce_mean(tf.square(y_array - pie_price))

train_step = 0
learn_rate = 0

if method == 1:
    learn_rate = 0.01
    train_step = 1001
elif method == 2:
    learn_rate = 0.001
    train_step = 2001
else:
    learn_rate = 0.001
    train_step = 4001

optimizer = tf.train.GradientDescentOptimizer(learn_rate)
train = optimizer.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(train_step):
    sess.run(train)
    if step % 100 == 0:
        print(f'step={step} loss={sess.run(loss)}')

_b = sess.run(b)
_w1 = sess.run(w1)

print(f'bias={_b} w1={_w1}')

sess.close()

best_fit = []
for value in pie_size:
    best_fit.append(_w1 * value + _b)

print(f'best_fit={best_fit}')

plt.figure()

plt.scatter(pie_size, pie_price, c='y', marker='o', label="pie")
plt.plot(pie_size, best_fit, color='b')

plt.show()
