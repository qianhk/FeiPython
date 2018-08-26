#!/usr/bin/env python3
# coding=utf-8

import os
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
import kaiMnist.conv.mnist_inference as mnist_inference

BATCH_SIZE = 100
LEARNING_RATE_BASE = 0.01
LEARNING_RATE_DECAY = 0.99

REGULARIZATION_RATE = 0.0001
TRAINING_STEPS = 10000
MOVING_AVERAGE_DECAY = 0.99

MODEL_SAVE_PATH = '../../logs/kaiConvMnist/'
MODEL_NAME = 'model.ckpt'


def train(mnist):
    x = tf.placeholder(tf.float32
                       , [BATCH_SIZE, mnist_inference.IMAGE_SIZE, mnist_inference.IMAGE_SIZE, mnist_inference.NUMBER_CHANNELS],
                       name='x-input')
    y_ = tf.placeholder(tf.float32, [BATCH_SIZE, mnist_inference.OUTPUT_NODE], name='y-input')

    regularizer = tf.contrib.layers.l2_regularizer(REGULARIZATION_RATE)
    y = mnist_inference.inference(x, True, regularizer)
    global_step = tf.Variable(0, trainable=False, name='globalStep')

    variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    # print(f'global_variables = {tf.global_variables()}\ntrainable_variables = {tf.trainable_variables()}')
    variables_averages_op = variable_averages.apply(tf.trainable_variables())

    # average_y = inference(x, variable_averages, weights1, biases1, weights2, biases2)
    average_y = y

    cross_entroy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y_, 1))
    cross_entroy_mean = tf.reduce_mean(cross_entroy)
    loss = cross_entroy_mean
    if regularizer is not None:
        loss += tf.add_n(tf.get_collection(tf.GraphKeys.LOSSES))

    # learning_rate = LEARNING_RATE_BASE
    learning_rate = tf.train.exponential_decay(LEARNING_RATE_BASE, global_step
                                               , mnist.train.num_examples / BATCH_SIZE, LEARNING_RATE_DECAY)

    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)

    # train_op = tf.group(train_step, variables_averages_op)
    with tf.control_dependencies([train_step, variables_averages_op]):
        train_op = tf.no_op(name='train')

    saver = tf.train.Saver()
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for i in range(TRAINING_STEPS):
            # print(f'global_step={sess.run(global_step)}')
            xs, ys = mnist.train.next_batch(BATCH_SIZE)
            reshaped_xs = np.reshape(xs,
                                     (BATCH_SIZE, mnist_inference.IMAGE_SIZE, mnist_inference.IMAGE_SIZE, mnist_inference.NUMBER_CHANNELS))
            _, loss_value, step = sess.run([train_op, loss, global_step], feed_dict={x: reshaped_xs, y_: ys})
            if i % 100 == 0:
                print(f'After {step} training step(s), loss on training is {loss_value}')
                saver.save(sess, os.path.join(MODEL_SAVE_PATH, MODEL_NAME), global_step=global_step)
        print(f'After last {step} training step(s), loss on training is {loss_value}')
        saver.save(sess, os.path.join(MODEL_SAVE_PATH, MODEL_NAME), global_step=global_step)


def main(argv=None):
    print(f'argv={argv}')
    mnist = input_data.read_data_sets('../../cache/mnist', one_hot=True)
    train(mnist)


if __name__ == '__main__':
    tf.app.run()
