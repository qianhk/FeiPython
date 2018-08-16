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

float_value = 123.4567
string_value = 'abc'
print('format={1:.2f} {0}'.format(string_value, float_value))

print(f'try_{float_value} \'str\'={string_value} {{abc}}')
print(f'试试_{float_value:.2f} str={string_value}')

for i in range(10):
    print('i: ' + str(i))

a, b = 5, 10
print(f'\na={a} b={b}')

a, b = b, a
print(f'after swap a={a} b={b}')

a = ['Python', 'is', 'awesome']
print(f'{" ".join(a)}')

a = [1, 2, 3, 1, 2, 3, 2, 2, 4, 5, 1]
print(f'a.count={a.count(8)} a.count(2)={a.count(2)} c.count(1)={a.count(1)} max={max(set(a), key = a.count)}')

from collections import Counter

cnt = Counter(a)
print(f'cnt.most_common(3)={cnt.most_common(3)}')

str1 = 'abcb'
str2 = 'bacb'

print(f'is Anagram: {Counter(str1) == Counter(str2)}')

a = 'abcdefghijklmnopqrstuvwxyz'
print(f'{a[::-1]}')

# for char in reversed(a):
#     print(char)

num = 123456789
print(int(str(num)[::-1]))

a = [5, 4, 3, 2, 1]
print(f'a[::-1]={a[::-1]}')

b = 6
print(f'4 < b < 7 : {4 < b < 7}')
print(f'1 == b < 20 : {1 == b < 20}')
