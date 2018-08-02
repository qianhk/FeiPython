#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import tensorflow as tf
from sklearn import datasets
import kaiFullNN.nn_from_mock_data_utils as kai

random_state = np.random.RandomState(2)
data, target = datasets.make_moons(200, noise=0.10, random_state=random_state)
target = np.array(target, dtype=np.float32)
data *= 5
m_x = data

m_target = np.matrix(target).T

# print('data=%s' % m_x)
# print('target=%s' % target)

hidden_layer_nodes = 5
v_w1 = tf.Variable(tf.random_normal([2, hidden_layer_nodes], 1), dtype=tf.float32)
b1 = tf.Variable(tf.random_normal([hidden_layer_nodes], 1), dtype=tf.float32)
v_w2 = tf.Variable(tf.random_normal([hidden_layer_nodes, 1]), dtype=tf.float32)
b2 = tf.Variable(tf.random_normal([1], 1), dtype=tf.float32)

h_x = tf.placeholder(shape=[None, 2], dtype=tf.float32)
h_target = tf.placeholder(shape=[None, 1], dtype=tf.float32)

activation = tf.nn.sigmoid
# activation = tf.nn.relu

z2 = tf.add(tf.matmul(h_x, v_w1), b1)  # (N, hidden_layer_nodes)
a2 = activation(z2)

z3 = tf.matmul(a2, v_w2)  # (N, 1)
a3 = activation(z3)

output = a3

loss = tf.square(h_target - output)
loss = tf.reduce_mean(loss)

learning_rate = 10.0
total_count = 10001
if activation == tf.nn.relu:
    learning_rate = 0.005
    total_count = 2_0001

optimizer = tf.train.GradientDescentOptimizer(learning_rate)
# optimizer = tf.train.AdamOptimizer(learning_rate)
train = optimizer.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

data_amount = len(data)
batch_size = 20

loss_vec = []

for step in range(total_count):
    # rand_index = np.random.choice(data_amount, size=batch_size)
    # tmp1 = var_x1[rand_index]
    # tmp2 = [tmp1]
    # x1 = np.transpose(tmp2)
    # x2 = np.transpose([var_x2[rand_index]])
    # y = np.transpose([target[rand_index]])
    feed = {h_x: m_x, h_target: m_target}
    sess.run(train, feed_dict=feed)
    if step % 1000 == 0:
        loss_value = sess.run(loss, feed_dict=feed)
        loss_vec.append(loss_value)
        print(f'step={step} b1={sess.run(b1)} b2={sess.run(b2)} loss={loss_value}')

_w1 = sess.run(v_w1).ravel()
_w2 = sess.run(v_w2).ravel()
print(f'last w1={_w1} w2={_w2}')

probabilities = sess.run(output, feed_dict={h_x: m_x}).ravel()

# print('target=\n%s\n predict=\n%s' % (target, probabilities))

class1_x = [x[0] for i, x in enumerate(data) if target[i] == 1]
class1_y = [x[1] for i, x in enumerate(data) if target[i] == 1]
class2_x = [x[0] for i, x in enumerate(data) if target[i] != 1]
class2_y = [x[1] for i, x in enumerate(data) if target[i] != 1]

visualization_frame, _ = kai.make_visualization_frame(class1_x, class1_y, class2_x, class2_y)
series_x1 = visualization_frame['x1']
series_x2 = visualization_frame['x2']
xx = np.c_[series_x1, series_x2]
visual_probabilities = sess.run(output, feed_dict={h_x: xx}).ravel()
visualization_frame['probabilities'] = visual_probabilities

sess.close()

kai.show_visualization_data(class1_x, class1_y, class2_x, class2_y
                            , loss_vec
                            , target, probabilities
                            , 'circle classify by nn'
                            , visualization_frame)
