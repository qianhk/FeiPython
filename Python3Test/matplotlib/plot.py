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
