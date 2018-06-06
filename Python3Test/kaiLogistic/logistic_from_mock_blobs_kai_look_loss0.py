#!/usr/bin/env python3
# coding=utf-8

# from http://lotabout.me/2018/Logistic-Regression-Notes/

import numpy as np
import matplotlib.pyplot as plt
import math

samples = [(-5, 1), (-20, 0), (-2, 1)]


def sigmoid(theta, x):
    return 1.0 / (1 + np.exp(- theta * x))


def cost(theta):
    diffs = [(sigmoid(theta, x) - y) for x, y in samples]
    return sum(diff * diff for diff in diffs) / len(samples) / 2


def log_loss(theta, x, y):
    tmp_sigmoid = sigmoid(theta, x)
    first = -y * np.log(tmp_sigmoid)
    second = (1 - y) * np.log(1 - tmp_sigmoid)
    return first - second


def cost2(theta):
    diffs = [log_loss(theta, x, y) for x, y in samples]
    return sum(diff for diff in diffs) / len(samples)


X = np.arange(-1, 1, 0.01)
Y = np.array([cost2(theta) for theta in X])
plt.plot(X, Y)
plt.show()
