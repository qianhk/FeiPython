#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt

data = [(-5, 1), (-20, 0), (-2, 1)]

var_x = np.array([x for x, y in data])
var_y = np.array([y for x, y in data])

print(var_x)
print(var_y)


def limit_min(array, min_value):
    tmp = np.array([x if x > min_value else min_value for x in array])
    return tmp


def limit_max(array, max_value):
    tmp = np.array([x if x < max_value else max_value for x in array])
    return tmp


def sigmoid(z):
    exp = np_exp(-z)
    return 1.0 / (1 + exp)


def np_exp(array):
    return np.exp(limit_max(array, 300))


# def log_cost(X, y):
#     first = np.multiply(-y, np.log(X))
#     second = np.multiply(1 - y, np.log(1 - X))
#     return np.sum(first - second) / len(X)

def np_log(array):
    return np.log(limit_min(array, 0.00001))


loss_type = 5


# 逻辑回归 损失函数 凸函数 证明
# 证明LogLoss是凸函数
# http://sofasofa.io/forum_main_post.php?postid=1000921
# http://lotabout.me/2018/Logistic-Regression-Notes/
def calc_loss(_b=0, _w1=0):
    result_mul = np.multiply(var_x, _w1)
    result_add = result_mul + _b
    result_sigmoid = sigmoid(result_add)

    if loss_type == 1 or loss_type == 2:
        if loss_type == 1:
            loss_array = np.square(result_add - var_y)  # linear regression square loss
        else:
            loss_array = np.square(result_sigmoid - var_y)  # logistic regression square loss
        return np.sqrt(np.mean(loss_array))
    elif loss_type == 3:
        h = np.zeros(len(var_y)) + _w1
        first = np.multiply(-var_y, np_log(h))  # use _w1 as 自变量
        second = np.multiply(1 - var_y, np_log(1 - h))
        loss_array = first - second
        return np.average(loss_array)
    elif loss_type == 4:
        loss_array = np.maximum(result_add, 0) - result_add * var_y + np.log(1 + np.exp(-np.abs(result_add)))
        return np.average(loss_array)
    else:
        # result_sigmoid = np.zeros(len(var_x1)) + _w1
        first = np.multiply(-var_y, np_log(result_sigmoid))  # logistic regression log loss
        second = np.multiply(1 - var_y, np_log(1 - result_sigmoid))
        loss_array = first - second
        # return np.sum(first - second) / len(first)
        return np.average(loss_array)


def predict(_x1, _x2, _b, _w1, _w2):
    result = _b + _x1 * _w1 + _x2 * _w2
    result_sigmoid = 1 / (1 + np_exp(-result))
    return result_sigmoid


if __name__ == '__main__':
    loss_vec = []

    max_n = 1
    b = 0
    test_range = np.arange(-max_n, max_n, 0.01)
    for step in test_range:
        loss = calc_loss(b, step)
        loss_vec.append(loss)
        # print('step=%d loss=%s' % (step, loss))

    plt.figure()
    plt.title('loss type: ' + str(loss_type))
    plt.plot(test_range, loss_vec, 'g-')
    plt.show()
