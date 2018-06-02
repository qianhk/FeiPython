#!/usr/bin/env python3
# coding=utf-8

import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
import kaiLogistic.logistic_from_mock_data_utils as kai

random_state = np.random.RandomState(2)
data, target = datasets.make_blobs(n_samples=20, n_features=2, centers=2, cluster_std=1.0, random_state=random_state)
# print('data=%s' % data)
# print('target=%s' % target)

var_x1 = [x[0] for i, x in enumerate(data)]
var_x2 = [x[1] for i, x in enumerate(data)]


def calc_loss(_b=0, _w1=0, _w2=0):
    result_mul1 = np.multiply(var_x1, _w1)
    result_mul2 = np.multiply(var_x2, _w2)
    result_add = result_mul1 + result_mul2 + _b
    result_sigmoid = 1 / (1 + np.exp(-result_add))

    loss_array = np.square(result_sigmoid - target)
    return np.sqrt(np.mean(loss_array))


def predict(_x1, _x2, _b, _w1, _w2):
    result = _b + _x1 * _w1 + _x2 * _w2
    result_sigmoid = 1 / (1 + np.exp(-result))
    return result_sigmoid


if __name__ == '__main__':
    loss_vec = []

    max_n = 200
    b = -10
    w2 = 20
    test_range = np.arange(-max_n, max_n, 1)
    for step in test_range:
        loss = calc_loss(b, step, w2)
        loss_vec.append(loss)
        # print('step=%d loss=%s' % (step, loss))

    plt.figure()
    plt.plot(test_range, loss_vec, 'g-')
    plt.show()

    class1_x = [x[0] for i, x in enumerate(data) if target[i] == 1]
    class1_y = [x[1] for i, x in enumerate(data) if target[i] == 1]
    class2_x = [x[0] for i, x in enumerate(data) if target[i] != 1]
    class2_y = [x[1] for i, x in enumerate(data) if target[i] != 1]

    w1 = 200
    # w1 = 50
    frame, _ = kai.make_visualization_frame(class1_x, class1_y, class2_x, class2_y)
    series_x1 = frame['x1']
    series_x2 = frame['x2']
    frame['probabilities'] = predict(series_x1, series_x2, b, w1, w2)

    kai.show_visualization_data(class1_x, class1_y, class2_x, class2_y
                                , None
                                , None, None
                                , 'Test RMSE Loss'
                                , frame)
