#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf
import numpy as np
from tensorflow.python.framework import ops
import matplotlib.pyplot as plt

# 造数据 y=Kx+3 (K=5)

ops.reset_default_graph()

sess = tf.Session()

# 数据数量
data_amount = 101

# 下面这个数据可以得到 K=5 学习率用0.005
# x_vals = np.random.normal(1, 0.1, data_amount)
# y_vals = np.add(np.repeat(5., data_amount), 3)

# 但下面这个数据 K=nan ? 学习率的影响太大了，比较适合用0.0001
x_vals = np.linspace(20, 200, data_amount)
y_vals = np.add(np.multiply(x_vals, 5), 3)

# print(x_vals)
# print(y_vals)

y_offset_vals = np.random.normal(0, 8, data_amount)
y_vals = np.add(y_vals, y_offset_vals)
# print(y_vals)


x_data = tf.placeholder(shape=[1], dtype=tf.float32, name='input')
y_target = tf.placeholder(shape=[1], dtype=tf.float32, name='output')

# 构造K
K = tf.Variable(tf.random_normal(mean=2, shape=[1]), name='k')
# b = tf.Variable(tf.random_normal(mean=20, shape=[1]), name='b')
b = tf.constant(3, dtype=tf.float32, name='b')

calcY = tf.add(tf.multiply(x_data, K), b, name='calcY')

loss = tf.square(y_target - calcY)

# print(loss)

init = tf.global_variables_initializer()
sess.run(init)

print('init K=' + str(sess.run(K)))

my_opt = tf.train.GradientDescentOptimizer(0.00001)
train_step = my_opt.minimize(loss)

loss_vec = []

for i in range(data_amount * 4):
    rand_index = np.random.choice(data_amount)
    x = [x_vals[rand_index]]
    y = [y_vals[rand_index]]
    sess.run(train_step, feed_dict={x_data: x, y_target: y})
    # print('step={} x={} y={}'.format((i + 1), x, y))

    tmp_loss = sess.run(loss, feed_dict={x_data: x, y_target: y})
    loss_vec.append(tmp_loss)

    if tmp_loss < 0.0001:
        print('tmp loss ok, step=%d k=%.4f loss=%.6f x=%.2f' % (i, sess.run(K), tmp_loss, x[0]))
        break

    if (i + 1) % 25 == 0:
        print('Step #' + str(i + 1) + ' K = ' + str(sess.run(K)) + ' b = ' + str(sess.run(b)))
        print('input=%.2f Loss = %s' % (x[0], str(sess.run(loss, feed_dict={x_data: x, y_target: y}))))

print('\nLast K = ' + str(sess.run(K)) + '  Loss = ' + str(sess.run(loss, feed_dict={x_data: [100], y_target: [503]})))

print('\nOver\n')

# writer = tf.summary.FileWriter("../logs/boardTest", tf.get_default_graph())
# writer.close()

output_graph_def = tf.graph_util.convert_variables_to_constants(sess, sess.graph_def,
                                                                output_node_names=['input', 'output', 'k', 'b',
                                                                                   'calcY'])
f = tf.gfile.FastGFile('../logs/kai_linear_only_mul.pb', mode='wb')
f.write(output_graph_def.SerializeToString())
f.close()

sess.close()

plt.plot(loss_vec, 'k-')

yticks = np.linspace(0, 5000, 11)
plt.yticks(yticks)
plt.title('Look Loss')
plt.xlabel('Generation')
plt.ylabel('Loss')
# plt.show()
