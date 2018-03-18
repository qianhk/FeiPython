#!/usr/bin/env python3
# coding=utf-8


import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

X = [[1, 2], [3, 4], [5, 6]]

ax = fig.add_subplot(121)
ax.imshow(X, cmap=plt.cm.gray)

x = np.linspace(-5, 5, 100)
y = x
X, Y = np.meshgrid(x, y)
result = np.sqrt(X ** 2 + Y ** 2)

ax = fig.add_subplot(122)
ax.imshow(result)

plt.show()
