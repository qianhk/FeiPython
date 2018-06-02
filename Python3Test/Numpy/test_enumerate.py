#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import pandas as pd


def show_predict_probability(frame):
    x1 = frame['x1']
    x2 = frame['x2']
    probability = frame['probabilities']
    class1_x = [x1[i] for i, x in enumerate(probability) if x >= 0.5]
    class1_y = [x2[i] for i, x in enumerate(probability) if x >= 0.5]
    class2_x = [x1[i] for i, x in enumerate(probability) if x < 0.5]
    class2_y = [x2[i] for i, x in enumerate(probability) if x < 0.5]
    print('class1_x = \n %s' % class1_x)
    print('class1_y = \n %s' % class1_y)
    print('class2_x = \n %s' % class2_x)
    print('class2_y = \n %s' % class2_y)


if __name__ == '__main__':
    frame = pd.DataFrame()
    n = 5
    npx1 = np.linspace(0, 9, n)
    npx2 = np.linspace(100, 109, n)
    X1, X2 = np.meshgrid(npx1, npx2)
    frame['x1'] = np.reshape(X1, n * n)
    frame['x2'] = np.reshape(X2, n * n)
    frame['probabilities'] = np.random.rand(n * n)
    print(frame)
    show_predict_probability(frame)
