#!/usr/bin/env python
# coding=utf-8

import numpy as np

A = [1, -1, 3]

a1 = np.abs(A).sum()
a2 = np.sum(np.abs(A))

A1 = [[1]]
A2 = [[-1]]
A3 = [[3]]

sum_abs = 2 * (np.abs(A1) + np.abs(A2) + np.abs(A3))
a11 = sum_abs[0, 0]
a12 = np.mean(sum_abs)

print(f'a1={a1} a2={a2} sum_abs={sum_abs} a11={a11} a12={a12}')
