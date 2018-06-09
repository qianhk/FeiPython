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

print('\na = %s type=%s\n' % (a, type(a)))
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
print('a @ c = %s' % (a @ c))

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

# 生成均值为loc，标准差为scale的正态分布矩阵，numpy中很多方法如果size不写则返回一个值
y = np.random.normal(10, 1, (2, 5))
print('\ny = %s\n' % y)
print('y.mean=%s y.std=%s' % (y.mean(), y.std()))

D = np.mat("1 2 3; 2 3 1; 3 1 2")
print('D.det = %s' % np.linalg.det(D))
# print('A.det = %s' % np.linalg.det(np.mat(a))) #LinAlgError: Last 2 dimensions of the array must be square
print('\nD = %s type = %s' % (D, type(D)))
D_I = D.I
print('D.I = %s type = %s' % (D_I, type(D_I)))
print('D * D.I = %s' % np.dot(D, D_I))
print('D.I * D = %s' % np.dot(D_I, D))

print('\neye(3) = %s' % (np.eye(3)))

M = np.array([1, 2, 3])
N = np.array([1, 0, 2])
print('\nM = %s    N = %s type(M)=%s' % (M, N, type(M)))

DOT_MN = np.dot(M, N)
print('dot(M,N)=%s  type=%s' % (DOT_MN, type(DOT_MN)))

DOT_MAT_MN = np.dot(np.mat(M), np.mat(N).T)
print('dot(mat(M), mat(N).T)=%s  type=%s' % (DOT_MAT_MN, type(DOT_MAT_MN)))

np_array = np.array([np.inf, -np.inf, np.nan, -128, 128])
print('np.nan_to_num=%s' % np.nan_to_num(np_array))
