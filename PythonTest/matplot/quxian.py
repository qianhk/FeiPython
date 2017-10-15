#!/usr/bin/env python
# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np

# a = np.linspace(0,10,100)
# b = np.exp(-a)
# plt.plot(a,b)
# plt.show()



# X = np.linspace(-400, 400, 10000)
# Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)
# plt.title('$f(x)=\\frac{1}{4}(x+4)(x+1)(x-2)$')
# plt.plot(X, Y, c = 'g')

X = np.linspace(-4 * 3.1415926, 4 * 3.1415926, 10000)
Y = np.sin(X)
plt.plot(X, Y)

plt.show()
