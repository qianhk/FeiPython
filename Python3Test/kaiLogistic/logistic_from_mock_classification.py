#!/usr/bin/env python3
# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from sklearn import datasets

data, target = datasets.make_classification(n_samples=1000, n_features=2, n_redundant=0, n_informative=1,
                                            n_clusters_per_class=1)
plt.scatter(data[:, 0], data[:, 1], marker='o', c=target)

plt.show()
