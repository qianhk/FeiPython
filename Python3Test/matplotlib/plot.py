#!/usr/bin/env python3
# coding=utf-8

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


# https://www.jianshu.com/p/8ed59ac76c06 中文显示问题
def getChineseFont():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc', size=15)


plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

y = [1, 15, 3, 6, 23]

plt.figure()
plt.title(u'绘制中文标题', fontproperties=getChineseFont())
plt.ylabel(u'Y轴label', fontproperties=getChineseFont())
plt.ylim(0, 30)
plt.yticks(range(0, 30, 5))
# plt.plot(range(0, 5), y, "r:o", label="折线图label")
plt.scatter(range(0, 5), y, color='m', label="散点图label")
# plt.scatter(range(0, 5), y, color='#00ff00', label="散点图label")
# plt.scatter(range(0, 5), y, color=(1.0, 0.5, 0.04), label="散点图label")
# plt.bar(range(0, 5), y, color='c', label="柱状图label")
# plt.barh(range(0, 5), y, color='y', label="条形图label")
plt.legend(loc='upper left', prop=getChineseFont())
# plt.grid(True)
plt.show()

import numpy as np
n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2 * X)

plt.axes([0.025, 0.025, 0.95, 0.95])

plt.plot(X, Y + 1, color='blue', alpha=1.00)
plt.fill_between(X, 1, Y + 1, color='blue', alpha=.25)

plt.plot(X, Y - 1, color='blue', alpha=1.00)
plt.fill_between(X, -1, Y - 1, (Y - 1) > -1, color='blue', alpha=.25)
plt.fill_between(X, -1, Y - 1, (Y - 1) < -1, color='red', alpha=.25)

plt.xlim(-np.pi, np.pi), plt.xticks([])
plt.ylim(-2.5, 2.5), plt.yticks([])
# savefig('../figures/plot_ex.png',dpi=48)
plt.show()
