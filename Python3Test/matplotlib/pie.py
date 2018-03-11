#!/usr/bin/env python3
# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np


def set_ch():
    from pylab import mpl
    mpl.rcParams['font.sans-serif'] = ['STHeiti']  # 指定默认字体 //findfont: Font family ['sans-serif'] not found
    mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# set_ch()

n = 5
# Z = np.random.uniform(0, 1, n)
list = np.array([1, 2, 3, 4])
print('Z= %s' % list)

# plt.pie(Z)
# plt.show()

labels = [u'First', 'Second', 'Third', 'Fourth']
colors = ['red', 'Yellow', 'blue', 'green']
explode = (0.15, 0, 0, 0)
plt.pie(list, explode=explode, labels=labels, colors=colors, startangle=60, labeldistance=1.1, pctdistance=0.6,
        autopct='%.1f%%')
plt.axis('equal')
plt.legend()
plt.show()
