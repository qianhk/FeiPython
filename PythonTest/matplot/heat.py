#!/usr/bin/env python
# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np

# a = np.linspace(-100, 100, 1000)
# # b = np.power(a, 3)
# b = np.log(a)
# plt.plot(a, b)

# a = np.linspace(0, 4)
# b = -4.9 * a * a + 14.7 * a + 18
# plt.plot(a, b)

# X = np.linspace(-400, 400, 10000)
# Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)
# plt.title('$f(x)=\\frac{1}{4}(x+4)(x+1)(x-2)$')
# plt.plot(X, Y, c = 'g')

# X = np.linspace(-4 * 3.1415926, 4 * 3.1415926, 10000)
# Y = np.sin(X)
# plt.plot(X, Y)

# a = 1
# t = np.linspace(0, 2 * np.pi, 1024)
# X = a * (2 * np.cos(t) - np.cos(2 * t))
# Y = a * (2 * np.sin(t) - np.sin(2 * t))
# plt.plot(Y, X, color='r')

# T = np.linspace(0, 2 * np.pi, 1024)
# plt.axes(polar=True)
# plt.plot(T, 1. - np.sin(T), color="r")

#面积2000，求周长最短 均值不等式 a+b≥2√(a*b)
X = np.linspace(30, 70, 10000)  # a==b且a44.72 周长最短
Y = 2000.0 / X  + X
plt.plot(X, Y)

plt.show()
