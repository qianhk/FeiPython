#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import tensorflow as tf

x0 = np.array([1, 1, 1, 1], dtype=np.float32)
x1 = np.array([0, 0, 1, 1], dtype=np.float32)
x2 = np.array([0, 1, 0, 1], dtype=np.float32)
target = np.array([0, 0, 0, 1], dtype=np.float32)

X = np.vstack((x0, x1, x2))
Target = np.matrix(target)

print(Target)
print(X)

W = tf.Variable(np.zeros((1, 3)), dtype=tf.float32)

Z = tf.matmul(W, X)

loss = tf.nn.sigmoid_cross_entropy_with_logits(logits=Z, labels=Target)
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
        print('step=%d W=%s loss=%s' % (
            step, sess.run(W), sess.run(loss)))

_W = sess.run(W).ravel()

sess.close()

print(f"last type(W)={type(_W)} W={_W}")
