#!/usr/bin/env python3
# coding=utf-8


import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
(C, S) = np.cos(X), np.sin(X)

# 这里用到了Matplotlib和numpy模块,linspace在(−π,π)之间分成共256个小段，
# 并把这256个值赋予X。C,S分别是cosine和sine值（X,C,S都是numpy数组）

fig = plt.figure()

# plt.plot(X, C, 'b-', lw=2.5)
# plt.plot(X, S, 'r-', lw=1.5)

plt.plot(X, C, 'b-', lw=2.5, label='cos')
plt.plot(X, S, 'r-.', lw=1.5, label='sin')

plt.legend(loc='upper left')

plt.ylim(C.min() * 1.2, C.max() * 1.2)
plt.xlim(X.min() * 1.2, X.max() * 1.2)

# plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi])
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'-π', r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$', r'$+\pi$'])
plt.yticks([-1, 0, 1])

ax = plt.gca()
ax.spines['right'].set_color('none')  # 先把右边和上边的边界设置为不可见
ax.spines['top'].set_color('none')

# ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))  # 然后把下边界和左边界移动到0点
# ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# 给特殊点添加注释
t = 2 * np.pi / 3

plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=1.0, linestyle="--")
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')  # 画出需要标注的点
plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot([t, t], [0, np.sin(t)], color='red', linewidth=1.0, linestyle="--")
plt.scatter([t, ], [np.sin(t), ], 50, color='red')
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# for label in ax.get_xticklabels() + ax.get_yticklabels():
#     label.set_fontsize(16)
#     label.set_bbox(dict(facecolor='w', edgecolor='None', alpha=0.4))

plt.show()
