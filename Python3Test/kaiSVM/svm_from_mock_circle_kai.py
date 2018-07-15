#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import tensorflow as tf
from sklearn import datasets
import kaiSVM.svm_from_mock_data_utils as kai

batch_size = 100

random_state = np.random.RandomState(2)
data, target = datasets.make_circles(n_samples=100, factor=0.5, noise=0.05, random_state=random_state)
target = np.array([1 if y == 1 else -1 for y in target], dtype=np.float32)
# print('data=%s' % data)
# print('target=%s' % target)

x_data = tf.placeholder(shape=[None, 2], dtype=tf.float32)
y_target = tf.placeholder(shape=[None, 1], dtype=tf.float32)

b = tf.Variable(tf.random_normal(shape=[1, batch_size]))

# Gaussian (RBF) kernel
gamma = tf.constant(-50.0)
dist = tf.reduce_sum(tf.square(x_data), 1)
dist = tf.reshape(dist, [-1, 1])
x_square = tf.matmul(x_data, tf.transpose(x_data))
subtract = tf.subtract(dist, tf.multiply(2., x_square))
sq_dists = tf.add(subtract, tf.transpose(dist))
# sq_dists = tf.add(tf.subtract(dist, tf.multiply(2., tf.matmul(x_data, tf.transpose(x_data)))), tf.transpose(dist))
my_kernel = tf.exp(tf.multiply(gamma, tf.abs(sq_dists)))

# Compute SVM Model
first_term = tf.reduce_sum(b)
b_vec_cross = tf.matmul(tf.transpose(b), b)
y_target_cross = tf.matmul(y_target, tf.transpose(y_target))
second_term = tf.reduce_sum(tf.multiply(my_kernel, tf.multiply(b_vec_cross, y_target_cross)))
loss = tf.negative(tf.subtract(first_term, second_term))

optimizer = tf.train.GradientDescentOptimizer(0.003)
train = optimizer.minimize(loss)

prediction_grid = tf.placeholder(shape=[None, 2], dtype=tf.float32)
rA = dist  # tf.reshape(tf.reduce_sum(tf.square(x_data), 1), [-1, 1])
rB = tf.reshape(tf.reduce_sum(tf.square(prediction_grid), 1), [-1, 1])
pred_sq_dist = tf.add(tf.subtract(rA, tf.multiply(2., tf.matmul(x_data, tf.transpose(prediction_grid)))),
                      tf.transpose(rB))
pred_kernel = tf.exp(tf.multiply(gamma, tf.abs(pred_sq_dist)))

prediction_output = tf.matmul(tf.multiply(tf.transpose(y_target), b), pred_kernel)
prediction = tf.sign(prediction_output - tf.reduce_mean(prediction_output))
prediction = tf.squeeze(prediction)
accuracy = tf.reduce_mean(tf.cast(tf.equal(prediction, tf.squeeze(y_target)), tf.float32))

sess = tf.Session()
sess.run(tf.global_variables_initializer())

data_amount = len(data)

loss_vec = []

for step in range(1001):
    rand_index = np.random.choice(data_amount, size=batch_size)
    x = data[rand_index]
    y = np.transpose([target[rand_index]])
    sess.run(train, feed_dict={x_data: x, y_target: y})
    if step % 200 == 0:
        loss_value = sess.run(loss, feed_dict={x_data: x, y_target: y})
        loss_vec.append(loss_value)
        acc_temp = sess.run(accuracy, feed_dict={x_data: x, y_target: y, prediction_grid: x})
        print(f'step={step} loss={loss_value} acc={acc_temp}')

_b = sess.run(b)
# print(f'last b={_b}')

target_t = np.transpose([target])
probabilities = sess.run(prediction, feed_dict={x_data: data, y_target: target_t, prediction_grid: data})

# print('target=\n%s\n predict=\n%s' % (target, probabilities))

class1_x = [x[0] for i, x in enumerate(data) if target[i] == 1]
class1_y = [x[1] for i, x in enumerate(data) if target[i] == 1]
class2_x = [x[0] for i, x in enumerate(data) if target[i] != 1]
class2_y = [x[1] for i, x in enumerate(data) if target[i] != 1]

visualization_frame, _, X1, X2 = kai.make_visualization_frame(class1_x, class1_y, class2_x, class2_y)
series_x1 = visualization_frame['x1']
series_x2 = visualization_frame['x2']
xx = np.c_[series_x1, series_x2]
visual_probabilities = sess.run(prediction, feed_dict={x_data: data, y_target: target_t, prediction_grid: xx})
visualization_frame['probabilities'] = visual_probabilities

sess.close()

kai.show_visualization_data(class1_x, class1_y, class2_x, class2_y
                            , loss_vec
                            , target, probabilities
                            , 'blobs kai linear svm'
                            , visualization_frame, X1, X2)
