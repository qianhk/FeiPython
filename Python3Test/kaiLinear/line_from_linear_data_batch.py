#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf
import numpy as np
import kaiLinear.line_from_linear_data_utils as kai
from tensorflow.python.tools.inspect_checkpoint import print_tensors_in_checkpoint_file

x_data_array, y_data_array = kai.get_linear_data()

# w = tf.Variable(0, dtype=tf.float32, name='w')
w = tf.get_variable('w', dtype=tf.float32, initializer=0.0)
# w = tf.get_variable('w', dtype=tf.float32, initializer=tf.constant(0, dtype=tf.float32))
b = tf.constant(50, dtype=tf.float32, name='b')

x_data = tf.placeholder(dtype=tf.float32, name='inputX')
y_target = tf.placeholder(dtype=tf.float32, name='yTarget')

y_calc = tf.add(tf.multiply(x_data, w), b, name='yCalc')

loss = tf.square(y_calc - y_target)
loss = tf.reduce_mean(loss)
optimizer = tf.train.GradientDescentOptimizer(0.000002)
train = optimizer.minimize(loss)

saver = tf.train.Saver()

sess = tf.Session()

ckpt_state = tf.train.get_checkpoint_state("../logs/line_batch_model")
print('ckpt_state:\n%s' % ckpt_state)

if ckpt_state and ckpt_state.model_checkpoint_path:
    print_tensors_in_checkpoint_file(ckpt_state.model_checkpoint_path, None, True, True)
    print('\n')
    saver.restore(sess, ckpt_state.model_checkpoint_path)
else:
    sess.run(tf.global_variables_initializer())

loss_vec = []

data_amount = len(x_data_array)
batch_size = 20


def save_current_model(step):
    saved_path = saver.save(sess, '../logs/line_batch_model/model', global_step=step)
    # print('save: step=%s path=%s' % (step, saved_path))


for step in range(200):
    step += 1
    rand_index = np.random.choice(data_amount, size=batch_size)
    x = x_data_array[rand_index]
    y = y_data_array[rand_index]
    sess.run(train, feed_dict={x_data: x, y_target: y})
    loss_value = sess.run(loss, feed_dict={x_data: x, y_target: y})
    loss_vec.append(loss_value)
    if step % 40 == 0:
        print('step=%d weight=%f bias=%f loss=%s' % (step, sess.run(w), sess.run(b), loss_value))
        save_current_model(step)

_w = sess.run(w)
_b = sess.run(b)

sess.close()

print('last W=%f B=%f' % (_w, _b))

kai.show_visualization_data(x_data_array, y_data_array, _w, _b, loss_vec, title='Batch Data')
