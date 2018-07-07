#!/usr/bin/env python3
# coding=utf-8


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib import cm

x = np.array([1, 2])
y = np.array([1, 2])
z = np.array([[1, -1], [-1, 1]])
# plt.xlim(1, 2)
# plt.ylim(1, 2)
colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
cmap = ListedColormap(colors[:len(np.unique(z))])
# plt.contour(x, y, z, cmap=cmap)
# plt.contourf(x, y, z, cmap=cm.PuBu_r)
plt.contour(x, y, z, 1)
plt.show()
