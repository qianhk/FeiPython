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

t = np.diag(a)
print('a diag = %s' % t)
print('a diag(t) = %s' % np.diag(t))

t = np.ones((3, 3))
t = np.diag(t)
print('a diag_ones = %s' % t)
print('a diag_dialog(ones) = %s' % np.diag(t))

print('')

b = np.array([(1, 2, 3), (4, 5, 6)], dtype=np.int32)

print('b=')
print(b)
print("a's ndim {}".format(b.ndim))
print("a's shape {}".format(b.shape))
print("a's size {}".format(b.size))
print("a's dtype {}".format(b.dtype))
print("a's itemsize {}".format(b.itemsize))

c = np.eye(4)
print(('np.eye = %s' % c))

print(f'a = {a}\na ** 2 = {a ** 2}\na ** 3 = {a ** 3}')
