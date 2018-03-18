#!/usr/bin/env python3
# coding=utf-8


from pylab import *
import matplotlib.pyplot as plt


def f(px, py): return (1 - px / 2 + px ** 5 + py ** 3) * np.exp(-px ** 2 - py ** 2)


def f2(px, py):
    tmp = np.sqrt(px ** 2 + py ** 2)
    # tmp *= 100
    return tmp


# n = 100
# x = np.linspace(-50, 5, n)
# y = np.linspace(-5, 5, n)
#
# X, Y = np.meshgrid(x, y)
#
# result = f2(X, Y)
#
# plt.imshow(result)
#
# plt.show()

X = [[1, 2], [3, 4], [5, 6]]
plt.imshow(X)
# plt.imshow(X, cmap=plt.cm.gray, interpolation='nearest')
# cmap=plt.cm.gray spring summer autumn winter hot cool
plt.colorbar(shrink=0.5)  # Bar为一半长度
plt.show()
