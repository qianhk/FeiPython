#!/usr/bin/env python3
# coding=utf-8

import time
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

import kaiMnist.conv.mnist_inference as mnist_inference
import kaiMnist.conv.mnist_train_entry as mnist_train

EVAL_INTERVAL_SECS = 10
BATCH_SIZE = 100


def evaluate(mnist):
    with tf.Graph().as_default() as g:
        x = tf.placeholder(tf.float32
                           , [None, mnist_inference.IMAGE_SIZE, mnist_inference.IMAGE_SIZE, mnist_inference.NUMBER_CHANNELS],
                           name='x-input')
        y_ = tf.placeholder(tf.float32, [None, mnist_inference.OUTPUT_NODE], name='y-input')
        reshaped_xs = np.reshape(mnist.validation.images,
                                 (-1, mnist_inference.IMAGE_SIZE, mnist_inference.IMAGE_SIZE, mnist_inference.NUMBER_CHANNELS))
        validate_feed = {x: reshaped_xs, y_: mnist.validation.labels}

        y = mnist_inference.inference(x, False, None)

        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        # saver = tf.train.Saver()

        variable_averages = tf.train.ExponentialMovingAverage(mnist_train.MOVING_AVERAGE_DECAY)
        variable_to_restore = variable_averages.variables_to_restore()
        print(f'variable_to_restore={variable_to_restore}')
        saver = tf.train.Saver(variable_to_restore)

        while True:
            with tf.Session() as sess:
                ckpt = tf.train.get_checkpoint_state(mnist_train.MODEL_SAVE_PATH)
                if ckpt and ckpt.model_checkpoint_path:
                    # print(f'checkpoint path: {ckpt.model_checkpoint_path}')
                    saver.restore(sess, ckpt.model_checkpoint_path)
                    global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
                    accuracy_score = sess.run(accuracy, feed_dict=validate_feed)
                    print(f'After {global_step} training step(s), validation accuracy = {accuracy_score}')
                else:
                    print('No checkpoint file found')
            time.sleep(EVAL_INTERVAL_SECS)


def main(argv=None):
    print(f'argv={argv}')
    mnist = input_data.read_data_sets('../../cache/mnist', one_hot=True)
    evaluate(mnist)


if __name__ == '__main__':
    tf.app.run()
