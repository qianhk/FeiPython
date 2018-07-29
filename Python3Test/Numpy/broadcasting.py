#!/usr/bin/env python3
# coding=utf-8

# https://www.jianshu.com/p/550c90dfffa0
# 如果两个数组的后缘维度（即从末尾开始算起的维度）的轴长度相等或其中一方的长度为1，则认为他们是广播兼容的，广播会在缺失和(或)长度为1的维度上进行。

import numpy as np

arr = np.arange(12).reshape(4, 3)
print(arr)  # (4, 3)
print(f'arr.ndim={arr.ndim}\n')

mean0 = arr.mean(0)  # (3,)
print(f'mean0={mean0}')

print(f'arr-mean0={arr - mean0}\n')

mean1 = arr.mean(1)  # (4,)
mean1 = mean1.reshape((4, 1))
print(f'mean1={mean1}')

print(f'arr-mean1={arr - mean1}')
