#!/usr/bin/env python3
# coding=utf-8

import numpy as np

a = np.array([1, 2, 3])

print('a=')
print(a)
print("a's ndim {}".format(a.ndim))
print("a's shape {}".format(a.shape))
print("a's size {}".format(a.size))
print("a's dtype {}".format(a.dtype))
print("a's itemsize {}".format(a.itemsize))

print('')

b = np.array([(1, 2, 3), (4, 5, 6)], dtype=np.int32)

print('b=')
print(b)
print("a's ndim {}".format(b.ndim))
print("a's shape {}".format(b.shape))
print("a's size {}".format(b.size))
print("a's dtype {}".format(b.dtype))
print("a's itemsize {}".format(b.itemsize))
