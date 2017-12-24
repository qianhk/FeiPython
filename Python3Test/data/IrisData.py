#!/usr/bin/env python3
# coding=utf-8

from sklearn import datasets

iris = datasets.load_iris()
digits = datasets.load_digits()

print(len(iris.data))
print(len(digits.data))

print(iris.data[0])
print(iris.target)
print(digits.target)

print(digits.images[0])
