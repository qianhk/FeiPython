#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics


def show_visualization_data(class1_x, class1_y, class2_x, class2_y
                            , log_losses
                            , target_series, probabilities,
                            title=None):
    plt.figure(figsize=(10, 8))

    if title is not None:
        plt.title(title)

    ax = plt.subplot(121)
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

# ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
# ax2 = plt.subplot2grid((3,3), (1,0), colspan=2)
# ax3 = plt.subplot2grid((3,3), (1, 2), rowspan=2)
# ax4 = plt.subplot2grid((3,3), (2, 0))
# ax5 = plt.subplot2grid((3,3), (2, 1))
