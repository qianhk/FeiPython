#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
import pandas as pd


# numpy.flatten() 与 numpy.ravel()的区别
# https://blog.csdn.net/iamzhangzhuping/article/details/52366568
def make_visualization_frame(class1_x, class1_y, class2_x, class2_y):
    min_x = min(min(class1_x), min(class2_x))
    min_y = min(min(class1_y), min(class2_y))
    max_x = max(max(class1_x), max(class2_x))
    max_y = max(max(class1_y), max(class2_y))
    # print('min=%s_%s max=%s_%s' % (min_x, min_y, max_x, max_y))
    # print('ceil min=%s_%s max=%s_%s' % (math.ceil(min_x), math.ceil(min_y), math.ceil(max_x), math.ceil(max_y)))
    n = int(max(max_x - min_x, max_y - min_y) * 100)
    xs = np.linspace(min_x, max_x, n)
    ys = np.linspace(min_y, max_y, n)
    X1, X2 = np.meshgrid(xs, ys)
    frame = pd.DataFrame()
    frame['x1'] = X1.ravel()  # np.reshape(X1, n * n)
    frame['x2'] = X2.ravel()  # np.reshape(X2, n * n)
    # print(frame)
    return frame, np.zeros(n * n), X1, X2


def show_visualization_data(class1_x, class1_y, class2_x, class2_y
                            , log_losses
                            , target_series, probabilities,
                            title=None, visualization_frame=None, x1=None, x2=None):
    # print('\nvisualization_frame=\n%s\n' % visualization_frame)

    plt.figure(figsize=(10, 8))

    if title is not None:
        plt.title(title)

    ax = plt.subplot(121)
    if visualization_frame is not None and x1 is not None and x2 is not None:
        show_predict_probability(ax, visualization_frame, x1, x2)

    ax.scatter(class1_x, class1_y, c='r', marker='o')
    ax.scatter(class2_x, class2_y, c='b', marker='x')

    min_x = min(min(class1_x), min(class2_x))
    min_y = min(min(class1_y), min(class2_y))
    max_x = max(max(class1_x), max(class2_x))
    max_y = max(max(class1_y), max(class2_y))
    accuracy = np.equal(target_series, np.round(probabilities)).astype(np.float32).mean()
    ax.text((max_x + min_x) / 2, min_y - (max_y - min_y) / 25, f'accuracy: {accuracy * 100:.4f}%%')

    if log_losses is not None:
        ax = plt.subplot(222)
        ax.plot(log_losses, color='m', linewidth=1)

    if target_series is not None and probabilities is not None:
        ax = plt.subplot(224)
        false_positive_rate, true_positive_rate, thresholds = metrics.roc_curve(
            target_series, probabilities)
        ax.plot(false_positive_rate, true_positive_rate, c='c', label="ROC Curve")
        ax.plot([0, 1], [0, 1], 'y:', label="Random Classifier")

        auc = metrics.roc_auc_score(target_series, probabilities)
        # print(f'\n accuracy={accuracy * 100:.4f}%%  auc={auc:.6f}')
        ax.text(0.6, -0.02, f'auc: {auc:.6f}')

    # plt.legend() # 打开可开启图例显示
    plt.show()


def show_predict_probability(ax, frame, X1, X2):
    probability = frame['probabilities']
    shape = X1.shape
    new_probability = np.array(probability)
    reshape_predict = new_probability.reshape(shape)
    ax.contour(X1, X2, reshape_predict, 0)
