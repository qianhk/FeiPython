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

    X = np.vstack((x0, x1, x2))
    Target = np.matrix(target)

    print(Target)
    print(X)

    W = tf.Variable(np.zeros((1, 3)), dtype=tf.float32)

    Z = tf.matmul(W, X)

    loss = tf.nn.sigmoid_cross_entropy_with_logits(logits=Z, labels=Target)
    loss = tf.reduce_mean(loss)
    optimizer = tf.train.GradientDescentOptimizer(200)
    train = optimizer.minimize(loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    loss_vec = []

    for step in range(401):
        sess.run(train)
        loss_vec.append(sess.run(loss))
        if step % 100 == 0:
            print('step=%d W=%s loss=%s' % (
                step, sess.run(W), sess.run(loss)))

    _W = sess.run(W).ravel()

    sess.close()

    # And W=[-75.  50.  50.]
    # Or [-25.  50.  50.]
    print(f"last type(W)={type(_W)} W={_W}")


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
