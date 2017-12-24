#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf

sess = tf.Session()

# relu = max(0, x)
print(sess.run(tf.nn.relu([-3, 3, 10])))

# relu6 = min(max(0, x), 6)
print(sess.run(tf.nn.relu6([-3, 3, 10])))

# sigmoid = 1/(1+exp(-x))
print(sess.run(tf.nn.sigmoid([-1.0, 0, 1.0])))

# tanh = ((exp(x) - exp(-x)) / (exp(x) + exp(-1)
print(sess.run(tf.nn.tanh([-1.0, 0, 1.0])))

# softsign = x / (abs(x) + 1)
print(sess.run(tf.nn.softsign([-1.0, 0, 1.0])))

# softplus = log(exp(x)+1) relu平滑版
print(sess.run(tf.nn.softplus([-1.0, 0, 1.0])))

#elu (exp(x)+1) if x < 0 else x
print(sess.run(tf.nn.elu([-1.0, 0, 1.0])))

sess.close()
