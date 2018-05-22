#!/usr/bin/env python3
# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
# import sklearn.datasets as datasets
from sklearn import datasets

x_vals, y_vals = datasets.make_circles(n_samples=100, factor=0.5, noise=0.05)
# print('x_vals=%s' % x_vals)
print('y_vals=%s' % y_vals)

# plt.scatter(x_vals[:, 0], x_vals[:, 1])

x_vals *= 100

class1_x = [x[0] for i, x in enumerate(x_vals) if y_vals[i] == 1]
class1_y = [x[1] for i, x in enumerate(x_vals) if y_vals[i] == 1]
class2_x = [x[0] for i, x in enumerate(x_vals) if y_vals[i] != 1]
class2_y = [x[1] for i, x in enumerate(x_vals) if y_vals[i] != 1]

plt.scatter(class1_x, class1_y, c='r', marker='o')
plt.scatter(class2_x, class2_y, c='b', marker='x')

plt.show()
