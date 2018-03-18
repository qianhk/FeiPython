#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt


def f(px, py):
    return np.sqrt(px ** 2 + py ** 2)


n = 100
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)

result = f(X, Y)

fig = plt.figure()

ax = fig.add_subplot(221)
ax.imshow(result, cmap=plt.cm.rainbow)

ax = fig.add_subplot(222)
ax.imshow(result, cmap=plt.cm.gray)

ax = fig.add_subplot(223)
ax.imshow(result, cmap=plt.cm.hot)

ax = fig.add_subplot(224)
ax.imshow(result, cmap=plt.cm.cool)

plt.show()
