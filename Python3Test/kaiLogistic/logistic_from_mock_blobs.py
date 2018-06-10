#!/usr/bin/env python3
# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
# import sklearn.datasets as datasets
from sklearn import datasets
import kaiLogistic.logistic_from_mock_data_utils as kai

random_state = np.random.RandomState(2)
data, target = datasets.make_blobs(n_samples=100, n_features=2, centers=2, cluster_std=1.5, random_state=random_state)
# print('data=%s' % data)
# print('target=%s' % target)

# plt.figure(figsize=(8, 12))
# ax = plt.subplot(211)
# ax.scatter(data[:, 0], data[:, 1], c=target)

class1_x = [x[0] for i, x in enumerate(data) if target[i] == 1]
class1_y = [x[1] for i, x in enumerate(data) if target[i] == 1]
class2_x = [x[0] for i, x in enumerate(data) if target[i] != 1]
class2_y = [x[1] for i, x in enumerate(data) if target[i] != 1]

plt.scatter(class1_x, class1_y, c='r', marker='o')
plt.scatter(class2_x, class2_y, c='b', marker='x')

plt.show()

kai.make_visualization_frame(class1_x, class1_y, class2_x, class2_y)
