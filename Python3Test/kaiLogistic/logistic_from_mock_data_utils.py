#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn import metrics
import pandas as pd


def make_visualization_frame(class1_x, class1_y, class2_x, class2_y):
    min_x = min(min(class1_x), min(class2_x))
    min_y = min(min(class1_y), min(class2_y))
    max_x = max(max(class1_x), max(class2_x))
    max_y = max(max(class1_y), max(class2_y))
    # print('min=%s_%s max=%s_%s' % (min_x, min_y, max_x, max_y))
    # print('ceil min=%s_%s max=%s_%s' % (math.ceil(min_x), math.ceil(min_y), math.ceil(max_x), math.ceil(max_y)))
    n = int(max(max_x - min_x, max_y - min_y) * 3)
    xs = np.linspace(min_x, max_x, n)
    ys = np.linspace(min_y, max_y, n)
    X1, X2 = np.meshgrid(xs, ys)
    frame = pd.DataFrame()
    frame['x1'] = np.reshape(X1, n * n)
    frame['x2'] = np.reshape(X2, n * n)
    # print(frame)
    return frame, np.zeros(n * n)


def show_visualization_data(class1_x, class1_y, class2_x, class2_y
                            , log_losses
                            , target_series, probabilities,
                            title=None, visualization_frame=None):
    # print('\nvisualization_frame=\n%s\n' % visualization_frame)

    plt.figure(figsize=(10, 8))

    if title is not None:
        plt.title(title)

    ax = plt.subplot(121)
    if visualization_frame is not None:
        show_predict_probability(ax, visualization_frame)

    ax.scatter(class1_x, class1_y, c='r', marker='o')
    ax.scatter(class2_x, class2_y, c='b', marker='x')

    if log_losses is not None:
        ax = plt.subplot(222)
        ax.plot(log_losses, color='m', linewidth=1)

    ax = plt.subplot(224)
    false_positive_rate, true_positive_rate, thresholds = metrics.roc_curve(
        target_series, probabilities)
    ax.plot(false_positive_rate, true_positive_rate, c='c', label="our model")
    ax.plot([0, 1], [0, 1], 'y:', label="random classifier")
    # ax.legend(loc=2)

    plt.show()


def show_predict_probability(ax, frame):
    x1 = frame['x1']
    x2 = frame['x2']
    probability = frame['probabilities']
    class1_x = [x1[i] for i, x in enumerate(probability) if x >= 0.5]
    class1_y = [x2[i] for i, x in enumerate(probability) if x >= 0.5]
    class2_x = [x1[i] for i, x in enumerate(probability) if x < 0.5]
    class2_y = [x2[i] for i, x in enumerate(probability) if x < 0.5]
    ax.scatter(class1_x, class1_y, c='r', alpha=0.2, marker='s')
    ax.scatter(class2_x, class2_y, c='b', alpha=0.2, marker='s')

# ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
# ax2 = plt.subplot2grid((3,3), (1,0), colspan=2)
# ax3 = plt.subplot2grid((3,3), (1, 2), rowspan=2)
# ax4 = plt.subplot2grid((3,3), (2, 0))
# ax5 = plt.subplot2grid((3,3), (2, 1))
