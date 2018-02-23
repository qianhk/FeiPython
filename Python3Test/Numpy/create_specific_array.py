#!/usr/bin/env python3
# coding=utf-8

import numpy as np

np.random.seed(4)

# 全为0
a = np.zeros((2, 3))
print('np.zeros((2,3)= \n{}\n'.format(a))

# 全为1
b = np.ones((2, 3), dtype=int)
print('np.ones((2,3))= \n{}\ntype={}'.format(b, type(b)))

c = np.empty((2, 3))
print('np.empty((2,3))= \n{}\n'.format(c))

# 1开头 后续以此在上一个值的基础上+0.3，直到小于2
d = np.arange(1, 2, 0.3)
print('np.arange(1, 2, 0.3)= \n{}\n'.format(d))

# 1开头 2最后，中间11的数字平分
e = np.linspace(1, 2, 11)
print('np.linspace(1, 2, 11)= \n{}\n'.format(e))

# 生成[0,1)之间的浮点数, ranf = random = sample = random_sample continuous uniform
f = np.random.random((2, 3))
print('np.random.random(2,3)= \n{}\nitem {} type={}, item {} type={}\n'
      .format(f, f[0, 1], type(f[0, 1]), f[0][1], type(f[0][1])))

# 生成[0,1)之间的浮点数 uniform distribution
h = np.random.rand(2, 4)
print('np.random.rand(2, 4) = %s\n' % h)

# 具有标准正太分布的样本 standard normal distribution 0为均值、1为标准差 N(0,1)
i = np.random.randn(2, 3)
print('np.random.randn(2,3) = %s\n' % i)

j = np.random.randint(10, 20, size=(2, 5))
print('np.random.randint = %s\n' % j)

x = np.random.choice(10, 5, False)
print('np.random.choice(5, 5, False) = %s\n' % x)

list = ['a', 'b', 'c', 'd', 'e']
x = np.random.choice(list, size=(3, 4), replace=True, p=[0.1, 0.6, 0.1, 0.1, 0.1])
print('np.random.choice(demo_list) = %s\n' % x)
