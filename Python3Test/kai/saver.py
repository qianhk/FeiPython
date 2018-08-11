#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf

print()
v = tf.Variable(0, dtype=tf.float32, name='v')
for var in tf.global_variables():
    print(f'first: {var}')

print()
ema = tf.train.ExponentialMovingAverage(0.99, name='ema')
maintain_averages_op = ema.apply(tf.global_variables())
for var in tf.global_variables():
    print(f'second: {var}')

print()
saver = tf.train.Saver()
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    sess.run(tf.assign(v, 10))
    sess.run(maintain_averages_op)
    saver.save(sess, '../logs/saver/model')
    print(f'{sess.run([v, ema.average(v)])}')
    print(f'{sess.run(ema.average(v))}')
