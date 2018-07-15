#!/usr/bin/env python
# coding=utf-8

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import time

np.random.seed(0)

b = tf.Variable(0, dtype=tf.float32)
w1 = tf.Variable(0, dtype=tf.float32)
w2 = tf.Variable(0, dtype=tf.float32)
w3 = tf.Variable(0, dtype=tf.float32)
w4 = tf.Variable(0, dtype=tf.float32)

pie_size = np.array([-2, -1, 0, 1, 2], dtype=np.float32)
pie_price = np.log((pie_size + 3) * 10)
pie_price += np.random.normal(0, 0.3, [5])
# print(pie_price)

regularization_strength = 0.2
regularization_result = regularization_strength \
                        * (tf.abs(w1) + tf.abs(w2) + tf.abs(w3) + tf.abs(w4))


def loss_for_underfitting():
    target = b + w1 * pie_size
    return tf.reduce_mean(tf.square(target - pie_price))


def loss_for_ok():
    target = b + w1 * pie_size + w2 * pie_size ** 2
    return tf.reduce_mean(tf.square(target - pie_price))


def loss_for_overfitting():
    target = b + w1 * pie_size + w2 * pie_size ** 2 + w3 * pie_size ** 3 + w4 * pie_size ** 4
    return tf.reduce_mean(tf.abs(target - pie_price))


def loss_for_overfitting_scale():
    # 2   4   8   16
    target = b + w1 * pie_size + w2 * pie_size ** 2 / 2 + w3 * pie_size ** 3 / 4 + w4 * pie_size ** 4 / 8
    return tf.reduce_mean(tf.abs(target - pie_price))


def loss_for_overfitting_regular():
    target = b + w1 * pie_size + w2 * pie_size ** 2 / 2 + w3 * pie_size ** 3 / 4 + w4 * pie_size ** 4 / 8
    return tf.reduce_mean(tf.abs(target - pie_price)) + regularization_result


method = 1

if method == 0:
    learn_rate = 0.01
    loss = loss_for_underfitting()
elif method == 1:
    learn_rate = 0.0001
    loss = loss_for_ok()
elif method == 2:
    learn_rate = 0.0001
    loss = loss_for_overfitting()
elif method == 10:
    learn_rate = 0.01
    loss = loss_for_overfitting_scale()
else:
    learn_rate = 0.001
    loss = loss_for_overfitting_regular()

optimizer = tf.train.GradientDescentOptimizer(learn_rate)
train = optimizer.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

step = 0
last_loss1 = 0
last_loss2 = 0
while True:
    step += 1
    sess.run(train)
    if step % 1_0000 == 0:
        loss_value = sess.run(loss)
        time_str = time.strftime("%H:%M:%S", time.localtime())  # %Y-%m-%d %H:%M:%S
        print(f'step={step} time={time_str} loss={loss_value:0.8f}'
              + f' bias={sess.run(b):0.4f} w1={sess.run(w1):0.4f} w2={sess.run(w2):0.4f} w3={sess.run(w3):0.4f} w4={sess.run(w4):0.4f}')
        if loss_value < 0.01:
            break
        if last_loss1 == last_loss2 and last_loss2 == loss_value:
            break
        last_loss2 = last_loss1
        last_loss1 = loss_value
    if step >= 50_0000:
        break

_b = sess.run(b)
_w1 = sess.run(w1)
_w2 = sess.run(w2)
_w3 = sess.run(w3)
_w4 = sess.run(w4)

print(f'bias={_b} w1={_w1} w2={_w2} w3={_w3} w4={_w4}')

sess.close()

best_fit = []
x_array = np.linspace(pie_size[0] - 1, pie_size[len(pie_size) - 1] + 1, 10000)
for x in x_array:
    if method < 10:
        best_fit.append(_b + _w1 * x + _w2 * x ** 2 + _w3 * x ** 3 + _w4 * x ** 4)
    else:
        best_fit.append(_b + _w1 * x + _w2 * x ** 2 / 2 + _w3 * x ** 3 / 4 + _w4 * x ** 4 / 8)

# print(f'best_fit={best_fit}')

show_plt = 1

if show_plt == 1:
    plt.figure()
plt.scatter(pie_size, pie_price, c='y', marker='o', label="pie")
plt.plot(x_array, best_fit, color='b')
plt.show()
