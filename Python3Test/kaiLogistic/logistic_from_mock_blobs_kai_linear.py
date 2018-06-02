#!/usr/bin/env python3
# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from sklearn import datasets
import kaiLogistic.logistic_from_mock_data_utils as kai

random_state = np.random.RandomState(2)
data, target = datasets.make_blobs(n_samples=20, n_features=2, centers=2, cluster_std=1.0, random_state=random_state)
# print('data=%s' % data)
# print('target=%s' % target)

class1_x = [x[0] for i, x in enumerate(data) if target[i] == 1]
class1_y = [x[1] for i, x in enumerate(data) if target[i] == 1]
class2_x = [x[0] for i, x in enumerate(data) if target[i] != 1]
class2_y = [x[1] for i, x in enumerate(data) if target[i] != 1]

b = tf.Variable(0, dtype=tf.float32, name='b')
w1 = tf.Variable([[0]], dtype=tf.float32, name='w1')
w2 = tf.Variable([[0]], dtype=tf.float32, name='w2')

x_data1 = tf.placeholder(shape=[None, 1], dtype=tf.float32)
x_data2 = tf.placeholder(shape=[None, 1], dtype=tf.float32)
y_target = tf.placeholder(shape=[None, 1], dtype=tf.float32)

result_matmul1 = tf.matmul(x_data1, w1)
result_matmul2 = tf.matmul(x_data2, w2)
result_add = result_matmul1 + result_matmul2 + b  # tf.add(tf.add(result_matmul1, result_matmul2), b)
result_sigmoid = 1 / (1 + np.exp(-result_add))

loss = tf.square(result_sigmoid - y_target)
loss = tf.reduce_mean(loss)

optimizer = tf.train.GradientDescentOptimizer(0.00003)
train = optimizer.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

loss_vec = []

data_amount = len(x_data_array)
batch_size = 20

for step in range(201):
    rand_index = np.random.choice(data_amount, size=batch_size)
    x = x_data_array[rand_index]
    x = np.mat(x)
    x = x.T
    y = np.transpose([y_data_array[rand_index]])
    sess.run(train, feed_dict={x_data: x, y_target: y})
    if step % 20 == 0:
        loss_value = sess.run(loss, feed_dict={x_data: x, y_target: y})
        loss_vec.append(loss_value)
        print('step=%d weight=%s bias=%s loss=%s' % (step, sess.run(w), sess.run(b), loss_value))

[[_w]] = sess.run(w)
_w1 = sess.run(w)
_w2 = _w1[0, 0]
_b = sess.run(b)

output_graph_def = tf.graph_util.convert_variables_to_constants(sess, sess.graph_def,
                                                                output_node_names=['inputX', 'yTarget', 'w', 'b',
                                                                                   'yCalc'])
gfile = tf.gfile.FastGFile('../logs/line_from_linear_data_batch_mat.pb', mode='wb')
gfile.write(output_graph_def.SerializeToString())
gfile.close()

sess.close()

print('last W=%f B=%f' % (_w, _b))


kai.show_visualization_data(class1_x, class1_y, class2_x, class2_y
                            , log_losses
                            , target_series, probabilities
                            , 'blobs pandas linear classifier'
                            , None)
