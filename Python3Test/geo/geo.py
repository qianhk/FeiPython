#!/usr/bin/env python3
# coding=utf-8

import random

# 初始点信息
a1 = 34.3752989239;
b1 = 108.9080291565;
# 中间点信息
a2 = 34.3740193255;
b2 = 108.9085977848;

for i in range(1, 1000):
    while a1 >= a2:  # 循环条件 经度未到达中间点时执行
        xa = round(random.uniform(0.2, 7))  # 随机数，用于模拟人跑动
        xb = round(random.uniform(12, 15))
        # 竖直移动
        a1 = round(a1 - 0.0000072 * xa, 10)
        b1 = round(b1 + 0.0000008 * xb, 10)
        # 输出信息
        print('<wpt lat="' + str(a1) + '"' + ' ' + 'lon="' + str(b1) + '">')
        print('</wpt>')

for i in range(1, 1000):
    xa = round(random.uniform(2, 8))
    xb = round(random.uniform(1, 3))
    # 水平移动
    a2 = round(a2 - 0.000003 * xa, 10)
    b2 = round(b2 - 0.000025 * xb, 10)
    print('<wpt lat="' + str(a2) + '"' + ' ' + 'lon="' + str(b2) + '">')
    print('</wpt>')
