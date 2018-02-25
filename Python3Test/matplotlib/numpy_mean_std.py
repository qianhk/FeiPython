#!/usr/bin/env python3
# coding=utf-8


import matplotlib.pyplot as plt
import numpy as np

loc = 10.0
scale = 1.0

# data = np.random.normal(loc, scale, size=6000)
#
# # http://blog.csdn.net/lanchunhui/article/details/50163669
# # 高斯分布（Gaussian Distribution）的概率密度函数（probability density function）
# x_data = np.linspace(data.min(), data.max())
# plt.plot(x_data, 1. / (np.sqrt(2 * np.pi) * scale) * np.exp(-(x_data - loc) ** 2 / (2 * scale ** 2)))
#
# count, bins, _ = plt.hist(data, 30, normed=True)
# # plt.plot(bins, 1. / (np.sqrt(2 * np.pi) * scale) * np.exp(-(bins - loc) ** 2 / (2 * scale ** 2)))
#
# plt.show()


# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
mu, sigma = 2, 0.5
v = np.random.normal(mu, sigma, 5000)
# Plot a normalized histogram with 50 bins
plt.hist(v, bins=50, normed=1)  # matplotlib version (plot)

# Compute the histogram with numpy and then plot it
(n, bins) = np.histogram(v, bins=50, normed=True)  # NumPy version (no plot)
plt.plot(.5 * (bins[1:] + bins[:-1]), n)
plt.show()
