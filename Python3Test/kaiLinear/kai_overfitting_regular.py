#!/usr/bin/env python
# coding=utf-8

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

method = 5

if method != 50:
    b = tf.Variable(0, dtype=tf.float32)
    w1 = tf.Variable(0, dtype=tf.float32)
    w2 = tf.Variable(0, dtype=tf.float32)
    w3 = tf.Variable(0, dtype=tf.float32)
    w4 = tf.Variable(0, dtype=tf.float32)
    w5 = tf.Variable(0, dtype=tf.float32)
    w6 = tf.Variable(0, dtype=tf.float32)
    w7 = tf.Variable(0, dtype=tf.float32)
    w8 = tf.Variable(0, dtype=tf.float32)
    w9 = tf.Variable(0, dtype=tf.float32)
    w10 = tf.Variable(0, dtype=tf.float32)
else:
    b = tf.Variable(155, dtype=tf.float32)
    w1 = tf.Variable(-2800, dtype=tf.float32)
    w2 = tf.Variable(16666, dtype=tf.float32)
    w3 = tf.Variable(-40000, dtype=tf.float32)
    w4 = tf.Variable(33333, dtype=tf.float32)
    w5 = tf.Variable(0, dtype=tf.float32)
    w6 = tf.Variable(0, dtype=tf.float32)
    w7 = tf.Variable(0, dtype=tf.float32)
    w8 = tf.Variable(0, dtype=tf.float32)
    w9 = tf.Variable(0, dtype=tf.float32)
    w10 = tf.Variable(0, dtype=tf.float32)

if method <= 2:
    # n = 14
    # pie_size = np.arange(1, n + 1, 1)
    # pie_price = np.log(pie_size) * 10 + 2
    # # pie_price += np.random.normal(0, 1.5, [n])
    pie_size = np.array([1, 1.5, 2, 2.5, 3], dtype=np.float32)
    pie_price = np.log(pie_size) * 1 + np.random.normal(0, 0.2, [5])
elif method <= 4:
    pie_size = np.array([1, 1.5, 2, 2.5, 3], dtype=np.float32)
    pie_price = np.log(pie_size) * 1 + np.random.normal(0, 0.2, [5])
else:
    pie_size = np.array([0.1, 0.2, 0.3, 0.4, 0.5], dtype=np.float32)
    pie_price = np.array([5, -5, 5, -5.0, 5.0], dtype=np.float32)


def loss_for_underfitting():
    target = b + w1 * pie_size
    return tf.reduce_mean(tf.square(target - pie_price))


def loss_for_ok():
    target = b + w1 * pie_size + w2 * pie_size ** 2
    return tf.reduce_mean(tf.square(target - pie_price))


def loss_for_overfitting1():
    target = b + w1 * pie_size + w2 * pie_size ** 2 + w3 * pie_size ** 3
    return tf.reduce_mean(tf.square(target - pie_price))


def loss_for_overfitting2():
    target = b + w1 * pie_size + w2 * pie_size ** 2 + w3 * pie_size ** 3 + w4 * pie_size ** 4
    return tf.reduce_mean(tf.abs(target - pie_price))
    # return tf.reduce_mean(tf.square(target - pie_price))


def loss_for_overfitting3():
    target = b + w1 * pie_size + w2 * (pie_size ** 2) + w3 * (pie_size ** 3) + w4 * (pie_size ** 4) \
             + w5 * (pie_size ** 5) + w6 * (pie_size ** 6) + w7 * (pie_size ** 7) \
             + w8 * (pie_size ** 8) + w9 * (pie_size ** 9) + w10 * (pie_size ** 10)
    return tf.reduce_mean(tf.square(target - pie_price))


regularization_strength = 0.2
regularization_result = regularization_strength \
                        * (tf.abs(w1) + tf.abs(w2) + tf.abs(w3)
                           + tf.abs(w4) + tf.abs(w5))

if method == 1:
    learn_rate = 0.01
    train_step = 1001
    loss = loss_for_underfitting()
elif method == 2:
    learn_rate = 0.003
    train_step = 10001
    loss = loss_for_ok()
elif method == 3:
    learn_rate = 0.0001
    train_step = 20001
    loss = loss_for_overfitting1()
elif method == 4:
    learn_rate = 0.00005
    train_step = 50001
    loss = loss_for_overfitting2()  # bias=0.1161179170012474 w1=0.12124264985322952 w2=0.09945085644721985 w3=0.01959029585123062 w4=-0.009515732526779175 loss=0.00019
    # loss += regularization_result
else:
    learn_rate = 1.9
    train_step = 10001
    loss = loss_for_overfitting2()

optimizer = tf.train.GradientDescentOptimizer(learn_rate)
train = optimizer.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(train_step):
    sess.run(train)
    if step % 1000 == 0:
        print(f'step={step} loss={sess.run(loss)} bias={sess.run(b)} w1={sess.run(w1)} w2={sess.run(w2)} w3={sess.run(w3)} w4={sess.run(w4)}')

_b = sess.run(b)
_w1 = sess.run(w1)
_w2 = sess.run(w2)
_w3 = sess.run(w3)
_w4 = sess.run(w4)
_w5 = sess.run(w5)
_w6 = sess.run(w6)
_w7 = sess.run(w7)
_w8 = sess.run(w8)
_w9 = sess.run(w9)
_w10 = sess.run(w10)

print(f'bias={_b} w1={_w1} w2={_w2} w3={_w3} w4={_w4} w5={_w5} w6={_w6} w7={_w7} w8={_w8} w9={_w9} w10={_w10}')

sess.close()

best_fit = []
x_array = np.linspace(pie_size[0] - 0.01, pie_size[len(pie_size) - 1] + 0.01, 10000)
for x in x_array:
    best_fit.append(_b + _w1 * x + _w2 * (x ** 2) + _w3 * (x ** 3) + _w4 * (x ** 4) + _w5 * (x ** 5)
                    + _w6 * (x ** 6) + _w7 * (x ** 7) + _w8 * (x ** 8) + _w9 * (x ** 9) + _w10 * (x ** 10))

# print(f'best_fit={best_fit}')

show_plt = 1

if show_plt == 1:
    plt.figure()
plt.scatter(pie_size, pie_price, c='y', marker='o', label="pie")
plt.plot(x_array, best_fit, color='b')
plt.show()
