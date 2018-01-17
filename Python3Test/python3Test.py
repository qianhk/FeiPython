#!/usr/bin/env python3
# coding=utf-8

import os
import numpy as np
import sys

print('PATH=')
print(os.environ['PATH'])


print(np.random.normal(3, 1, 50))

print(np.repeat(3, 50))

print('\nsys.version=%s\n\nsys.version_info=%s' % (sys.version, sys.version_info))

# print('DYLD_LIBRARY_PATH=')
# print(os.environ['DYLD_LIBRARY_PATH'])

# print('PYTHONPATH=')
# print(os.environ['PYTHONPATH'])







