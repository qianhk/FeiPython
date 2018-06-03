#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import tensorflow as tf
from sklearn import datasets
import kaiLogistic.logistic_from_mock_data_utils as kai

random_state = np.random.RandomState(2)
data, target = datasets.make_blobs(n_samples=20, n_features=2, centers=2, cluster_std=1.0, random_state=random_state)
target = np.array(target, dtype=np.float32)
# print('data=%s' % data)
# print('target=%s' % target)


b = tf.Variable(1, dtype=tf.float32, name='b')
w1 = tf.Variable([[1]], dtype=tf.float32, name='w1')
w2 = tf.Variable([[1]], dtype=tf.float32, name='w2')

x_data1 = tf.placeholder(shape=[None, 1], dtype=tf.float32)
x_data2 = tf.placeholder(shape=[None, 1], dtype=tf.float32)
y_target = tf.placeholder(shape=[None, 1], dtype=tf.float32)

result_matmul1 = tf.matmul(x_data1, w1)
result_matmul2 = tf.matmul(x_data2, w2)
result_add = result_matmul1 + result_matmul2 + b  # tf.add(tf.add(result_matmul1, result_matmul2), b)
result_sigmoid = 1.0 / (1 + tf.exp(-result_add))

first = tf.multiply(-target, tf.log(result_sigmoid))
second = tf.multiply(1 - target, tf.log(1 - result_sigmoid))
loss = tf.reduce_mean(first - second)

optimizer = tf.train.GradientDescentOptimizer(0.3)
train = optimizer.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

var_x1 = np.array([x[0] for i, x in enumerate(data)])
var_x2 = np.array([x[1] for i, x in enumerate(data)])

data_amount = len(var_x1)
batch_size = 10

loss_vec = []

for step in range(2001):
    rand_index = np.random.choice(data_amount, size=batch_size)
    tmp1 = var_x1[rand_index]
    tmp2 = [tmp1]
    x1 = np.transpose(tmp2)
    x2 = np.transpose([var_x2[rand_index]])
    y = np.transpose([target[rand_index]])
    sess.run(train, feed_dict={x_data1: x1, x_data2: x2, y_target: y})
    if step % 20 == 0:
        loss_value = sess.run(loss, feed_dict={x_data1: x1, x_data2: x2, y_target: y})
        loss_vec.append(loss_value)
        print('step=%d w1=%s w2=%s b=%s loss=%s' % (step, sess.run(w1)[0, 0], sess.run(w2)[0, 0], sess.run(b), loss_value))

[[_w1]] = sess.run(w1)
[[_w2]] = sess.run(w2)
_b = sess.run(b)
print('last W1=%f W2=%f B=%f' % (_w1, _w2, _b))

x1 = np.transpose([var_x1])
x2 = np.transpose([var_x2])
probabilities = sess.run(result_sigmoid, feed_dict={x_data1: x1, x_data2: x2}).T[0]

# print('target=\n%s\n predict=\n%s' % (target, probabilities))

class1_x = [x[0] for i, x in enumerate(data) if target[i] == 1]
class1_y = [x[1] for i, x in enumerate(data) if target[i] == 1]
class2_x = [x[0] for i, x in enumerate(data) if target[i] != 1]
class2_y = [x[1] for i, x in enumerate(data) if target[i] != 1]

visualization_frame, _ = kai.make_visualization_frame(class1_x, class1_y, class2_x, class2_y)
series_x1 = visualization_frame['x1']
series_x2 = visualization_frame['x2']
x1 = np.transpose([series_x1])
x2 = np.transpose([series_x2])
visual_probabilities = sess.run(result_sigmoid, feed_dict={x_data1: x1, x_data2: x2}).T[0]
visualization_frame['probabilities'] = visual_probabilities

sess.close()

kai.show_visualization_data(class1_x, class1_y, class2_x, class2_y
                            , loss_vec
                            , target, probabilities
                            , 'blobs kai linear classifier'
                            , visualization_frame)
