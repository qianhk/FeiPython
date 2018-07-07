#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import tensorflow as tf
from sklearn import datasets
import kaiSVM.svm_from_mock_data_utils as kai

random_state = np.random.RandomState(2)
data, target = datasets.make_blobs(n_samples=123, n_features=2, centers=2, cluster_std=1.6, random_state=random_state)
target = np.array([1 if y == 1 else -1 for y in target], dtype=np.float32)
# print('data=%s' % data)
# print('target=%s' % target)

x_data = tf.placeholder(shape=[None, 2], dtype=tf.float32)
y_target = tf.placeholder(shape=[None, 1], dtype=tf.float32)

A = tf.Variable(tf.random_normal(shape=[2, 1]))
b = tf.Variable(tf.random_normal(shape=[1, 1]))

model_output = tf.subtract(tf.matmul(x_data, A), b)

l2_norm = tf.reduce_sum(tf.square(A))

alpha = tf.constant([10.01])
classification_term = tf.reduce_mean(tf.maximum(0., tf.subtract(1., tf.multiply(model_output, y_target))))
loss = tf.add(classification_term, tf.multiply(alpha, l2_norm))

prediction = tf.sign(model_output)
# accuracy = tf.reduce_mean(tf.cast(tf.equal(prediction, y_target), tf.float32))

optimizer = tf.train.GradientDescentOptimizer(0.003)
train = optimizer.minimize(loss)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

data_amount = len(data)
batch_size = 20

loss_vec = []

for step in range(5001):
    rand_index = np.random.choice(data_amount, size=batch_size)
    x = data[rand_index]
    y = np.transpose([target[rand_index]])
    sess.run(train, feed_dict={x_data: x, y_target: y})
    if step % 200 == 0:
        loss_value = sess.run(loss, feed_dict={x_data: x, y_target: y})
        loss_vec.append(loss_value)
        print('step=%d A=%s b=%s loss=%s' % (
            step, sess.run(A), sess.run(b), loss_value))

_a = sess.run(A)
_b = sess.run(b)
print('last A=%s b=%f' % (_a, _b))

probabilities = sess.run(prediction, feed_dict={x_data: data}).T[0]

# print('target=\n%s\n predict=\n%s' % (target, probabilities))

class1_x = [x[0] for i, x in enumerate(data) if target[i] == 1]
class1_y = [x[1] for i, x in enumerate(data) if target[i] == 1]
class2_x = [x[0] for i, x in enumerate(data) if target[i] != 1]
class2_y = [x[1] for i, x in enumerate(data) if target[i] != 1]

visualization_frame, _, X1, X2 = kai.make_visualization_frame(class1_x, class1_y, class2_x, class2_y)
series_x1 = visualization_frame['x1']
series_x2 = visualization_frame['x2']
xx = np.c_[series_x1, series_x2]
visual_probabilities = sess.run(prediction, feed_dict={x_data: xx}).T[0]
visualization_frame['probabilities'] = visual_probabilities

sess.close()

kai.show_visualization_data(class1_x, class1_y, class2_x, class2_y
                            , loss_vec
                            , target, probabilities
                            , 'blobs kai linear svm'
                            , visualization_frame, X1, X2)
