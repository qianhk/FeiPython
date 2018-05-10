#!/usr/bin/env python3
# coding=utf-8


import numpy as np
import matplotlib.pyplot as plt


def one(x):
    return 1 / x


def two(x):
    return -1 / (x * x)


# data = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
data_a = np.arange(2, 12, 1)
print('data_a = %s' % data_a)
one_a = one(data_a)
two_a = two(data_a)

plt.plot(range(len(data_a)), one_a, 'r')
plt.plot(range(len(data_a)), two_a, 'b')
plt.show()

data_b = np.arange(1, 12)
print('data_b = %s' % data_b)
one_b = np.log(data_b)
two_b = np.log(data_b + 10)
plt.plot(range(len(data_b)), one_b, 'r')
plt.plot(range(len(data_b)), two_b, 'b')
plt.show()

# plt.axis('off')
# plt.xticks([])
# plt.yticks([])

# frame = plt.gca()
# frame.axes.get_yaxis().set_visible(False)
# frame.axes.get_xaxis().set_visible(False)
