#!/usr/bin/env python3
# coding=utf-8


import numpy as np

base_data = (np.random.random((5, 5)) - 0.5) * 100
print("base_data = \n{}\n".format(base_data))

print("np.amin(base_data) = {}".format(np.amin(base_data)))
print("np.amax(base_data) = {}".format(np.amax(base_data)))
print("np.average(base_data) = {}".format(np.average(base_data)))
print("np.sum(base_data) = {}".format(np.sum(base_data)))
print("np.sin(base_data) = \n{}".format(np.sin(base_data)))

# a = np.array([[1, 2, 3], [4, 5, 6]])
a = np.arange(1, 7).reshape(2, 3)

b = np.array([[2, 1, 0], [1, 1, 1]])

c = a.transpose()

print('\na = %s\n' % a)
print('b = %s\n' % b)

print('a + 1 = %s' % (a + 1))
print('a * 2 = %s' % (a * 2))
print('a * b = %s' % (a * b))
print('a + b = %s' % (a + b))
print('np.multiply(a, b) = %s' % (np.multiply(a, b)))
print('np.multiply(np.mat(a), np.mat(b)) = %s' % (np.multiply(np.mat(a), np.mat(b))))
print('np.mat(a) * np.mat(b) = %s' % (np.mat(a) * np.mat(c)))

print('c = %s' % c)
print('a.T = %s' % a.T)
print('dot(a, c) = %s\n' % np.dot(a, c))

print('sum=%s min=%s max=%s mean=%s var=%s std=%s\n' % (a.sum(), a.min(), a.max(), a.mean(), a.var(), a.std()))

print('np.hstack = %s\n' % np.hstack((a, b)))
print('np.vstack = %s\n' % np.vstack((a, b)))
print('np.hsplit(a,3) = %s\n' % np.hsplit(a, 3))
print('np.vsplit(a,2) = %s\n' % np.vsplit(a, 2))

print('np.diag(a) = %s' % np.diag(a))
print('diag(diag(a)) = %s' % np.diag(np.diag(a)))

x = np.arange(10)

print('x = %s\n' % x)
print('x[2] = %s\n' % x[2])
print('x[-2] = %s\n' % x[-2])
print('x[2:5] = %s\n' % x[2: 5])
print('x[::-1] = %s\n' % x[::-1])
print('x[::-2] = %s\n' % x[::-2])

indexs = [2, 3, 4]
print('x[indexs]=%s' % (x * 2)[indexs])
x[::2] = [-1, -2, -3, -4, -5]
print('x after::2 = %s\n' % x)
print('x[::1] = %s\n' % x[::2])

print('a[1] = %s\n' % a[1])
print('a[1, :] = %s\n' % a[1, :])
print('a[:, 1] = %s\n' % a[:, 1])
print('a[1:3, 1:3] = %s\n' % a[1:3, 1:3])

x = np.arange(12).reshape(3, 4)
x = x > 4
print('x = %s\n' % x)
print('bools.any = %s\n' % x.any())
print('bools.all = %s\n' % x.all())

print('type(a) = %s' % type(a))
print('type((np.mat(a)) = %s' % type(np.mat(a)))

print('\na = %s\n' % a)
print("a's ndim {}".format(a.ndim))
print("a's shape {}".format(a.shape))
print("a's size {}".format(a.size))
print("a's dtype {}".format(a.dtype))
print("a's itemsize {}".format(a.itemsize))
