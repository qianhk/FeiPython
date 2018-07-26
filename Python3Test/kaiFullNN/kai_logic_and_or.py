#!/usr/bin/env python3
# coding=utf-8

import argparse
import numpy as np
import tensorflow as tf


def test_logic_and_or(arg_type):
    x0 = np.array([1, 1, 1, 1], dtype=np.float32)
    x1 = np.array([0, 0, 1, 1], dtype=np.float32)
    x2 = np.array([0, 1, 0, 1], dtype=np.float32)
    if arg_type == 'AND':
        target = np.array([0, 0, 0, 1], dtype=np.float32)
    elif arg_type == 'OR':
        target = np.array([0, 1, 1, 1], dtype=np.float32)
    else:
        print('test type error')
        return

    m_x = np.vstack((x0, x1, x2)).T
    m_target = np.matrix(target).T

    print(m_x)
    print(m_target)

    v_w = tf.Variable(np.zeros((3, 1)), dtype=tf.float32)
    h_x = tf.placeholder(shape=[None, 3], dtype=tf.float32)
    h_target = tf.placeholder(shape=[None, 1], dtype=tf.float32)

    z = tf.matmul(h_x, v_w)

    loss = tf.nn.sigmoid_cross_entropy_with_logits(logits=z, labels=h_target)
    loss = tf.reduce_mean(loss)
    optimizer = tf.train.GradientDescentOptimizer(200)
    train = optimizer.minimize(loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    loss_vec = []

    for step in range(401):
        feed_dict = {h_x: m_x, h_target: m_target}
        sess.run(train, feed_dict)
        loss_vec.append(sess.run(loss, feed_dict=feed_dict))
        if step % 100 == 0:
            print('step=%d W=%s loss=%s' % (
                step, sess.run(v_w).ravel(), sess.run(loss, feed_dict=feed_dict)))

    _w = sess.run(v_w).ravel()

    sess.close()

    # And W=[-75.  50.  50.]
    # Or [-25.  50.  50.]
    print(f"last type(W)={type(_w)} W={_w}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', default='AND', type=str, help='测试训练类型')
    args = parser.parse_args()
    # print(f'args={args}')
    arg_type = args.type
    if arg_type is None:
        print('need type argument')
    else:
        test_logic_and_or(arg_type.upper())
