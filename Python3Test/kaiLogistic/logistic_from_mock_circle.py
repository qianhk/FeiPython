#!/usr/bin/env python3
# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
# import sklearn.datasets as datasets
from sklearn import datasets

data, target = datasets.make_circles(n_samples=100, factor=0.5, noise=0.05)
# print('data=%s' % data)
print('target=%s' % target)

# plt.scatter(data[:, 0], data[:, 1])

data *= 100

class1_x = [x[0] for i, x in enumerate(data) if target[i] == 1]
class1_y = [x[1] for i, x in enumerate(data) if target[i] == 1]
class2_x = [x[0] for i, x in enumerate(data) if target[i] != 1]
class2_y = [x[1] for i, x in enumerate(data) if target[i] != 1]

plt.scatter(class1_x, class1_y, c='r', marker='o')
plt.scatter(class2_x, class2_y, c='b', marker='x')

plt.show()
