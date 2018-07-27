#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import tensorflow as tf
from sklearn import datasets

random_state = np.random.RandomState(2)
data, target = datasets.make_circles(n_samples=100, factor=0.5, noise=0.05, random_state=random_state)
target = np.array(target, dtype=np.float32)
data *= 5
# x0 = np.ones(100, dtype=np.float32)
# print(x0)
# m_x = np.vstack((x0, data.T))
m_x = data.T
# print('data=%s' % m_x)
# print('target=%s' % target)

hidden_layer_nodes = 2
v_w1 = tf.Variable(np.zeros((hidden_layer_nodes, 2)), dtype=tf.float32)
b1 = tf.Variable(np.zeros(hidden_layer_nodes), dtype=tf.float32)
v_w2 = tf.Variable(np.zeros((1, 2)), dtype=tf.float32)
b2 = tf.Variable(np.zeros(1), dtype=tf.float32)
h_x = tf.placeholder(shape=[2, None], dtype=tf.float32)
h_target = tf.placeholder(shape=[1, None], dtype=tf.float32)

z2 = tf.add(tf.matmul(v_w1, h_x), b1)  # (hidden_layer_nodes, N)
a2 = tf.sigmoid(z2)

a22 = tf.stack([x0, a2])

z3 = tf.matmul(v_w2, a22)  # (1, N)
a3 = tf.sigmoid(z2)  # (1, N)

loss = tf.nn.sigmoid_cross_entropy_with_logits(logits=z3, labels=h_target)

loss = tf.reduce_mean(loss)

optimizer = tf.train.GradientDescentOptimizer(0.1)
train = optimizer.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

data_amount = len(data)
batch_size = 20

loss_vec = []

for step in range(2001):
    # rand_index = np.random.choice(data_amount, size=batch_size)
    # tmp1 = var_x1[rand_index]
    # tmp2 = [tmp1]
    # x1 = np.transpose(tmp2)
    # x2 = np.transpose([var_x2[rand_index]])
    # y = np.transpose([target[rand_index]])
    feed = {h_x: m_x, h_target: target}
    sess.run(train, feed_dict=feed)
    if step % 100 == 0:
        loss_value = sess.run(loss, feed_dict=feed)
        loss_vec.append(loss_value)
        print(f'step={step} w1={sess.run(v_w1)} w2={sess.run(v_w2)} loss={loss_value}')

_w1 = sess.run(v_w1)
_w2 = sess.run(v_w2)
print(f'last w1={_w1} w2={_w2}')

# print('target=\n%s\n predict=\n%s' % (target, probabilities))


sess.close()
