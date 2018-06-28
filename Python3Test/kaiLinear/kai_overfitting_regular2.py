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

pie_size = np.array([-0.2, -0.1, 0, 0.1, 0.2], dtype=np.float32)
pie_price = np.array([5, -5, 5, -5.0, 5.0], dtype=np.float32)

regularization_strength = 0.001
regularization_result = regularization_strength \
                        * (tf.abs(w1) + tf.abs(w2) + tf.abs(w3) + tf.abs(w4))


def loss_for_overfitting():
    target = b + w1 * pie_size + w2 * pie_size ** 2 + w3 * pie_size ** 3 + w4 * pie_size ** 4
    return tf.reduce_mean(tf.abs(target - pie_price))


def loss_for_overfitting_scale():
    # 0.2     0.04    0.008   0.0016
    # 0.1    0.01   0.001  0.0001
    target = b + w1 * pie_size + w2 * pie_size ** 2 * 10 + w3 * pie_size ** 3 * 100 + w4 * pie_size ** 4 * 1000
    return tf.reduce_mean(tf.abs(target - pie_price))


def loss_for_overfitting_regular():
    target = b + w1 * pie_size + w2 * pie_size ** 2 * 10 + w3 * pie_size ** 3 * 100 + w4 * pie_size ** 4 * 1000
    return tf.reduce_mean(tf.abs(target - pie_price)) + regularization_result


method = 2

if method == 1:
    learn_rate = 0.000001
    loss = loss_for_overfitting()
elif method == 2:
    learn_rate = 0.05
    loss = loss_for_overfitting_scale()
else:
    learn_rate = 0.05
    loss = loss_for_overfitting_regular()
    # loss += regularization_result

optimizer = tf.train.GradientDescentOptimizer(learn_rate)
train = optimizer.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

step = 0
while True:
    step += 1
    sess.run(train)
    if step % 10000 == 0:
        loss_value = sess.run(loss)
        time_str = time.strftime("%H:%M:%S", time.localtime())  # %Y-%m-%d %H:%M:%S
        print(f'step={step} time={time_str} loss={loss_value:0.5f}'
              + f' bias={sess.run(b):0.2f} w1={sess.run(w1):0.2f} w2={sess.run(w2):0.2f} w3={sess.run(w3):0.2f} w4={sess.run(w4):0.2f}')
        # 如果要小于0.01 对于method2，当learn_rate = 0.01 需要88万次训练，如果提高learn_rate，则loss到达一定值的时候不会再降低
        if loss_value < 0.1:
            break
    if step >= 150000:
        break

_b = sess.run(b)
_w1 = sess.run(w1)
_w2 = sess.run(w2)
_w3 = sess.run(w3)
_w4 = sess.run(w4)

print(f'bias={_b} w1={_w1} w2={_w2} w3={_w3} w4={_w4}')

sess.close()

best_fit = []
x_array = np.linspace(pie_size[0] - 0.01, pie_size[len(pie_size) - 1] + 0.01, 10000)
for x in x_array:
    best_fit.append(_b + _w1 * x + _w2 * x ** 2 * 10 + _w3 * x ** 3 * 100 + _w4 * x ** 4 * 1000)

# print(f'best_fit={best_fit}')

show_plt = 1

if show_plt == 1:
    plt.figure()
plt.scatter(pie_size, pie_price, c='y', marker='o', label="pie")
plt.plot(x_array, best_fit, color='b')
plt.show()
