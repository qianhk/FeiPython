#!/usr/bin/env python
# coding=utf-8

from sklearn.externals import joblib
import coremltools
import tensorflow as tf

# 读取训练好的模型
# classifier = joblib.load('../logs/fully_connected_feed/model.ckpt')

saver = tf.train.Saver()
sess = tf.Session()
classifier = saver.restore(sess, '../logs/fully_connected_feed/model.ckpt')

# 生成模型的输入参数名称，总共有64个参数，所以我们生成的参数名称如下
# feature_0, feature_1 ... feature_63
feature_names = ["feature_" + str(i) for i in range(28 * 28)]

# 将模型转换为coreml的格式，并保存下来
coreml_model = coremltools.converters.sklearn.convert(classifier, feature_names, "digit")
coreml_model.save("../logs/model.mlmodel")
