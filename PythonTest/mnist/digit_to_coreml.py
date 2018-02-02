#!/usr/bin/env python
# coding=utf-8

import coremltools
from sklearn.externals import joblib
from sklearn import datasets, svm
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

X = digits.data
y = digits.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# 读取训练好的模型
classifier = joblib.load('../logs/digits.pkl')

# 生成模型的输入参数名称，总共有64个参数，所以我们生成的参数名称如下
# feature_0, feature_1 ... feature_63
feature_names = ["feature_" + str(i) for i, x in enumerate(X_train[0])]

# 将模型转换为coreml的格式，并保存下来
coreml_model = coremltools.converters.sklearn.convert(classifier, feature_names, "digit")
coreml_model.save("../logs/digits.mlmodel")
