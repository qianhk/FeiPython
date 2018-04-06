#!/usr/bin/env python3
# coding=utf-8

import os
import numpy as np
import sys

print('PATH=')
print(os.environ['PATH'])

print(np.random.normal(3, 1, 50))

print(np.repeat(3, 50))

print('\nsys.version = %s\n\nsys.version_info = %s\n' % (sys.version, sys.version_info))

# print('DYLD_LIBRARY_PATH=')
# print(os.environ['DYLD_LIBRARY_PATH'])

# print('PYTHONPATH=')
# print(os.environ['PYTHON PATH'])

print('os.system(\'id\') = %s\n' % str(os.system('id')))

print('------ Data Structures ------')

squares = []
for x in range(10):
    squares.append(x ** 2)

print('squares1=%s' % squares)

squares = list(map(lambda x: x ** 2, range(10)))
print('squares2=%s' % squares)

squares = [x ** 2 for x in range(10)]
print('squares3=%s' % squares)

print('\n------ Lambda Expressions ------')


def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)

print('f(0)=%s  f(1)=%s' % (f(0), f(1)))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print('pairs=%s' % pairs)
