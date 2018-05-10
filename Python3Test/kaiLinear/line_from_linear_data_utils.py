#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt


def get_linear_data():
    mock_data = np.genfromtxt('../data/linear_data.csv', delimiter=',', skip_header=1, dtype=float)
    x_data_array = np.array(mock_data[:, 0])
    y_data_array = np.array(mock_data[:, 1])
    return x_data_array, y_data_array


def show_visualization_data(x_data_array, y_data_array, w, b, loss_vec, title=None):
    best_fit = []
    for x in x_data_array:
        best_fit.append(w * x + b)

    plt.figure()

    if title is not None:
        plt.title(title)

    ax = plt.subplot(121)
    ax.scatter(x_data_array, y_data_array, color='y', label="样本", linewidths=0.5)
    ax.plot(x_data_array, best_fit, color='b', linewidth=2)

    if loss_vec is not None:
        ax = plt.subplot(122)
        ax.plot(loss_vec, color='g', linewidth=1)
        ax.set_ylim(0, 1000)

    plt.show()
