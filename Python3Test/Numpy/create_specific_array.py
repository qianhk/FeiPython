#!/usr/bin/env python3
# coding=utf-8

import numpy as np

a = np.zeros((2, 3))
print('np.zeros((2,3)= \n{}\n'.format(a))

b = np.ones((2, 3), dtype=int)
print('np.ones((2,3))= \n{}\ntype={}'.format(b, type(b)))

c = np.empty((2, 3))
print('np.empty((2,3))= \n{}\n'.format(c))

d = np.arange(1, 2, 0.3)
print('np.arange(1, 2, 0.3)= \n{}\n'.format(d))

e = np.linspace(1, 2, 11)
print('np.linspace(1, 2, 11)= \n{}\n'.format(e))

f = np.random.random((2, 3))
print('np.random.random(2,3)= \n{}\nitem {} type={}, item {} type={}\n'
      .format(f, f[0, 1], type(f[0, 1]), f[0][1], type(f[0][1])))
