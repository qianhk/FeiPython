#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf

v = tf.Variable(0, dtype=tf.float32, name='v')
ema = tf.train.ExponentialMovingAverage(0.99, name='ema')
print(ema.variables_to_restore())

saver = tf.train.Saver(ema.variables_to_restore())
# saver = tf.train.Saver({'v/ema': v})
with tf.Session() as sess:
    saver.restore(sess, '../logs/saver/model')
    print(f'v={sess.run(v)}')  # 0.09999990463256836
