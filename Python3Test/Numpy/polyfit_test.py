#!/usr/bin/env python
# coding=utf-8


import numpy as np
import matplotlib.pyplot as plt

CALIBRATE_X = [0.1, 0.2, 0.3, 0.4, 0.5]
CALIBRATE_Y = [5, -5, 5, -5.0, 5.0]
z1 = np.polyfit(CALIBRATE_X, CALIBRATE_Y, 4)
print(f'z1={z1}')  # [33333.33333333 - 40000.          16666.66666667 - 2800.            155.]
p1 = np.poly1d(z1)

best_fit = []
x_array = np.linspace(CALIBRATE_X[0] - 0.01, CALIBRATE_X[len(CALIBRATE_X) - 1] + 0.01, 10000)
y = []
for i in x_array:
    best_fit.append(p1(i))

plt.scatter(CALIBRATE_X, CALIBRATE_Y, c='y', marker='o', label="pie")
plt.plot(x_array, best_fit)
plt.show()
