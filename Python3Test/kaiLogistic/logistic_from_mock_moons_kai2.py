#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import tensorflow as tf
from sklearn import datasets
import kaiLogistic.logistic_from_mock_data_utils as kai

random_state = np.random.RandomState(1)
data, target = datasets.make_moons(200, noise=0.20, random_state=random_state)
target = np.array(target, dtype=np.float32)
# print('data=%s' % data)
# print('target=%s' % target)

data *= 5

b = tf.Variable(0, dtype=tf.float32)
w1 = tf.Variable([[0]], dtype=tf.float32)
w2 = tf.Variable([[0]], dtype=tf.float32)
w3 = tf.Variable([[0]], dtype=tf.float32)
w4 = tf.Variable([[0]], dtype=tf.float32)
w5 = tf.Variable([[0]], dtype=tf.float32)
w6 = tf.Variable([[0]], dtype=tf.float32)
w7 = tf.Variable([[0]], dtype=tf.float32)
w8 = tf.Variable([[0]], dtype=tf.float32)
w9 = tf.Variable([[0]], dtype=tf.float32)
w10 = tf.Variable([[0]], dtype=tf.float32)
w11 = tf.Variable([[0]], dtype=tf.float32)
w12 = tf.Variable([[0]], dtype=tf.float32)

x_data1 = tf.placeholder(shape=[None, 1], dtype=tf.float32)
x_data2 = tf.placeholder(shape=[None, 1], dtype=tf.float32)
y_target = tf.placeholder(shape=[None, 1], dtype=tf.float32)

use_method = 3

if use_method == 1:
    result_matmul1 = tf.matmul(x_data1, w1)
    result_matmul2 = tf.matmul(x_data2, w2)
    result_add = result_matmul1 + result_matmul2 + b
elif use_method == 2:
    result_matmul1 = tf.matmul(x_data1 ** 2, w1)
    result_matmul2 = tf.matmul(x_data2 ** 2, w2)
    result_add = result_matmul1 + result_matmul2 + b
elif use_method == 3:
    result_1 = tf.matmul(x_data1, w1)
    result_2 = tf.matmul(x_data2, w2)
    result_3 = tf.matmul(x_data1 ** 2, w3)
    result_4 = tf.matmul(x_data2 ** 2, w4)
    result_5 = x_data1 ** 3 * w5
    result_6 = x_data2 ** 3 * w6
    result_7 = x_data1 ** 4 * w7
    result_8 = x_data2 ** 4 * w8
    result_9 = x_data1 ** 5 * w9
    result_10 = x_data2 ** 5 * w10
    result_11 = x_data1 ** 6 * w11
    result_12 = x_data2 ** 6 * w12
    result_add = b + result_1 + result_2 + result_3 + result_4 + result_5 \
                 + result_6 + result_7 + result_8 + result_9 + result_10 \
                 + result_11 + result_12

loss = tf.nn.sigmoid_cross_entropy_with_logits(logits=result_add, labels=y_target)

loss = tf.reduce_mean(loss)

optimizer = tf.train.GradientDescentOptimizer(0.00001)
train = optimizer.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

var_x1 = np.array([x[0] for i, x in enumerate(data)])
var_x2 = np.array([x[1] for i, x in enumerate(data)])

data_amount = len(var_x1)
batch_size = 20

loss_vec = []

for step in range(100001):
    rand_index = np.random.choice(data_amount, size=batch_size)
    tmp1 = var_x1[rand_index]
    tmp2 = [tmp1]
    x1 = np.transpose(tmp2)
    x2 = np.transpose([var_x2[rand_index]])
    y = np.transpose([target[rand_index]])
    sess.run(train, feed_dict={x_data1: x1, x_data2: x2, y_target: y})
    if step % 200 == 0:
        loss_value = sess.run(loss, feed_dict={x_data1: x1, x_data2: x2, y_target: y})
        loss_vec.append(loss_value)
        print('step=%d w1=%s w2=%s b=%s loss=%s' % (
            step, sess.run(w1)[0, 0], sess.run(w2)[0, 0], sess.run(b), loss_value))

[[_w1]] = sess.run(w1)
[[_w2]] = sess.run(w2)
_b = sess.run(b)
print('last W1=%f W2=%f B=%f' % (_w1, _w2, _b))

result_sigmoid = tf.sigmoid(result_add)

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
