#!/usr/bin/env python
# coding=utf-8

from sklearn.externals import joblib
from sklearn import datasets, svm
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

# 对数据进行分割，使用2/3的数据进行训练，1/3的数据进行测试
# train_test_split是
# X_train : 训练用的图片数据
# y_train : 训练用的已分类的图片类别
# X_train : 测试用的图片数据
# y_train : 测试时用于对比测试结果的已分类图片类别
X = digits.data
y = digits.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# 初始化一个SVC（Support Vector Classification）支持向量机分类器
classifier = svm.SVC(gamma=0.001)

# 使用训练数据进行训练
classifier.fit(X_train, y_train)

# 查看模型在测试数据上的预测准确度
score = classifier.score(X_test, y_test)
print(score)
# 0.96327212020033393

# 保存模型
joblib.dump(classifier, '../logs/digits.pkl')
