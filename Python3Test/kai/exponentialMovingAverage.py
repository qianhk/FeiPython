#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf

v1 = tf.Variable(0, dtype=tf.float32)
step = tf.Variable(0, trainable=False)

ema = tf.train.ExponentialMovingAverage(0.99, step)
maintain_averages_op = ema.apply([v1])

with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)

    print(f'{sess.run([v1, ema.average(v1)])}')  # [0.0, 0.0]

    sess.run(tf.assign(v1, 5))
    sess.run(maintain_averages_op)  # min{0.99, (1+step)/(10+step)} = 0.1
    print(f'{sess.run([v1, ema.average(v1)])}')  # [5.0, 4.5]  0.1*0+0.9*5=4.5

    sess.run(tf.assign(step, 10000))
    sess.run(tf.assign(v1, 10))
    sess.run(maintain_averages_op)  # min{0.99, (1+10000) / (10 + 10000)} = 0.99
    print(f'{sess.run([v1, ema.average(v1)])}')  # [10.0, 4.5549998]   0.99*4.5+0.01*10=4.555

    sess.run(maintain_averages_op)
    print(f'{sess.run([v1, ema.average(v1)])}')  # [10.0, 4.6094499]  0.99*4.555+0.01*10=4.60945
