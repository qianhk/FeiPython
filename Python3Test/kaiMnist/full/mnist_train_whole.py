#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

INPUT_NODE = 28 * 28
OUTPUT_NODE = 10

LAYER1_NODE = 500
BATCH_SIZE = 100
LEARNING_RATE_BASE = 0.8
LEARNING_RATE_DECAY = 0.99

REGULARIZATION_RATE = 0.0001
TRAINING_STEPS = 11000
MOVING_AVERAGE_DECAY = 0.99


def inference(input_tensor, avg_class, weights1, biases1, weights2, biases2):
    if avg_class is None:
        layer1_z = tf.matmul(input_tensor, weights1) + biases1
        layer1 = tf.nn.relu(layer1_z)
        return tf.matmul(layer1, weights2) + biases2
        # return tf.matmul(input_tensor, weights2) + biases2
    else:
        layer1 = tf.nn.relu(tf.matmul(input_tensor, avg_class.average(weights1)) + avg_class.average(biases1))
        return tf.matmul(layer1, avg_class.average(weights2)) + avg_class.average(biases2)


def train(mnist):
    x = tf.placeholder(tf.float32, [None, INPUT_NODE], name='x-input')
    y_ = tf.placeholder(tf.float32, [None, OUTPUT_NODE], name='y-input')

    weights1 = tf.Variable(tf.truncated_normal([INPUT_NODE, LAYER1_NODE], stddev=0.1), name='weights1')
    biases1 = tf.Variable(tf.constant(0.1, shape=[LAYER1_NODE]), name='biases1')

    weights2 = tf.Variable(tf.truncated_normal([LAYER1_NODE, OUTPUT_NODE], stddev=0.1), name='weights2')
    biases2 = tf.Variable(tf.constant(0.1, shape=[OUTPUT_NODE]), name='biases2')
    y = inference(x, None, weights1, biases1, weights2, biases2)

    global_step = tf.Variable(0, trainable=False, name='globalStep')
    variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    # print(f'global_variables = {tf.global_variables()}\ntrainable_variables = {tf.trainable_variables()}')
    variables_averages_op = variable_averages.apply(tf.trainable_variables())

    # average_y = inference(x, variable_averages, weights1, biases1, weights2, biases2)
    average_y = y

    cross_entroy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y_, 1))
    cross_entroy_mean = tf.reduce_mean(cross_entroy)

    regularizer = tf.contrib.layers.l2_regularizer(REGULARIZATION_RATE)
    regularization = regularizer(weights1) + regularizer(weights2)
    loss = cross_entroy_mean + regularization

    # learning_rate = LEARNING_RATE_BASE
    learning_rate = tf.train.exponential_decay(LEARNING_RATE_BASE, global_step
                                               , mnist.train.num_examples / BATCH_SIZE, LEARNING_RATE_DECAY)

    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)

    train_op = tf.group(train_step, variables_averages_op)
    # with tf.control_dependencies([train_step, variables_averages_op]):
    #     train_op = tf.no_op(name='train')

    correct_prediction = tf.equal(tf.argmax(average_y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        validate_feed = {x: mnist.validation.images, y_: mnist.validation.labels}
        for i in range(TRAINING_STEPS):
            # print(f'global_step={sess.run(global_step)}')
            if i % 1000 == 0:
                validate_acc = sess.run(accuracy, feed_dict=validate_feed)
                print(f'After {i} training step(s), validation accuracy is {validate_acc}'
                      f' learning_rate={sess.run(learning_rate)}')
            xs, ys = mnist.train.next_batch(BATCH_SIZE)
            sess.run(train_step, feed_dict={x: xs, y_: ys})

        test_feed = {x: mnist.test.images, y_: mnist.test.labels}
        test_acc = sess.run(accuracy, feed_dict=test_feed)
        print(f'After {TRAINING_STEPS} training step(s), test accuracy is {test_acc}')


def main(argv=None):
    print(f'argv={argv}')
    mnist = input_data.read_data_sets('../../cache/mnist', one_hot=True)
    train(mnist)


if __name__ == '__main__':
    tf.app.run()
