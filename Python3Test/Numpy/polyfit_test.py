#!/usr/bin/env python
# coding=utf-8


import numpy as np
import matplotlib.pyplot as plt

# CALIBRATE_X = [-0.2, -0.1, 0, 0.1, 0.2]
# CALIBRATE_Y = [5, -5, 5, -5.0, 5.0]
CALIBRATE_X = [-2, -1, 0, 1, 2]
CALIBRATE_Y = [2.83180094, 3.1157794, 3.69481874, 4.3611474, 4.47229052]
z1 = np.polyfit(CALIBRATE_X, CALIBRATE_Y, 4)
print(f'z1={z1}')  # [  3.33333333e+04   9.97099527e-12  -1.33333333e+03   3.43344866e-13 5.00000000e+00]
p1 = np.poly1d(z1)

best_fit = []
x_array = np.linspace(CALIBRATE_X[0] - 0.01, CALIBRATE_X[len(CALIBRATE_X) - 1] + 0.01, 10000)
y = []
for i in x_array:
    best_fit.append(p1(i))

plt.scatter(CALIBRATE_X, CALIBRATE_Y, c='y', marker='o', label="pie")
plt.plot(x_array, best_fit)
plt.show()
