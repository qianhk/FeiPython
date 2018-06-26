#!/usr/bin/env python
# coding=utf-8

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

b = tf.Variable(0, dtype=tf.float32)
w1 = tf.Variable(0, dtype=tf.float32)
w2 = tf.Variable(0, dtype=tf.float32)
w3 = tf.Variable(0, dtype=tf.float32)
w4 = tf.Variable(0, dtype=tf.float32)
w5 = tf.Variable(0, dtype=tf.float32)

method = 3

if method != 3:
    n = 14
    pie_size = np.arange(1, n + 1, 1)
    pie_price = np.log(pie_size) * 10 + 2
    # pie_price += np.random.normal(0, 1.5, [n])
else:
    pie_size = np.array([1, 2, 3])
    pie_price = np.log(pie_size) * 1


def loss_for_underfitting():
    target = b + w1 * pie_size
    return tf.reduce_mean(tf.square(target - pie_price))


def loss_for_ok():
    target = b + w1 * pie_size + w2 * pie_size ** 2
    return tf.reduce_mean(tf.square(target - pie_price))


def loss_for_overfitting():
    target = b + w1 * pie_size + w2 * pie_size ** 2 + w3 * pie_size ** 3 + w4 * pie_size ** 4 + w5 * pie_size ** 5
    return tf.reduce_mean(tf.square(target - pie_price))


if method == 1:
    learn_rate = 0.01
    train_step = 1001
    loss = loss_for_underfitting()
elif method == 2:
    learn_rate = 0.003
    train_step = 10001
    loss = loss_for_ok()
else:
    learn_rate = 0.00001
    train_step = 10001
    loss = loss_for_overfitting()

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
_w2 = sess.run(w2)
_w3 = sess.run(w3)
_w4 = sess.run(w4)
_w5 = sess.run(w5)

print(f'bias={_b} w1={_w1} w2={_w2} w3={_w3} w4={_w4} w5={_w5}')

sess.close()

best_fit = []
for size in pie_size:
    best_fit.append(_b + _w1 * size + _w2 * size ** 2 + _w3 * size ** 3 + _w4 * size ** 4 + _w5 * size ** 5)

print(f'best_fit={best_fit}')

show_plt = 1

if show_plt == 1:
    plt.figure()
    plt.scatter(pie_size, pie_price, c='y', marker='o', label="pie")
    plt.plot(pie_size, best_fit, color='b')
    plt.show()
