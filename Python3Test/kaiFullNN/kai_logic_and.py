#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import tensorflow as tf

x1 = np.array([0, 0, 1, 1], dtype=np.float32)
x2 = np.array([0, 1, 0, 1], dtype=np.float32)
target = np.array([0, 0, 0, 1], dtype=np.float32)

w1 = tf.Variable(0, dtype=tf.float32, name='w1')

w2 = tf.Variable(0, dtype=tf.float32, name='w2')

b = tf.Variable(0., name='b', dtype=tf.float32)

z_array = w1 * x1 + w2 * x2 + b

loss = tf.nn.sigmoid_cross_entropy_with_logits(logits=z_array, labels=target)
loss = tf.reduce_mean(loss)
optimizer = tf.train.GradientDescentOptimizer(200)
train = optimizer.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

loss_vec = []

for step in range(401):
    sess.run(train)
    loss_vec.append(sess.run(loss))
    if step % 100 == 0:
        print('step=%d w1=%f w2=%f bias=%f loss=%s' % (
            step, sess.run(w1), sess.run(w2), sess.run(b), sess.run(loss)))

_w1 = sess.run(w1)
_w2 = sess.run(w2)
_b = sess.run(b)

sess.close()

print('last W1=%f W2=%f B=%f' % (_w1, _w2, _b))
