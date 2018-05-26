#!/usr/bin/env python3
# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import pandas as pd
import math
from tensorflow.python.data import Dataset
from sklearn import metrics
from sklearn import datasets
import kaiLogistic.logistic_from_mock_data_utils as kai

pd.options.display.float_format = '{:.6f}'.format

random_state = np.random.RandomState(2)
data, target = datasets.make_blobs(n_samples=100, n_features=2, centers=2, cluster_std=1.0, random_state=random_state)
# print('data=%s' % data)
# print('target=%s' % target)

plt.figure(figsize=(8, 12))

data *= 5

class1_x = [x[0] for i, x in enumerate(data) if target[i] == 1]
class1_y = [x[1] for i, x in enumerate(data) if target[i] == 1]
class2_x = [x[0] for i, x in enumerate(data) if target[i] != 1]
class2_y = [x[1] for i, x in enumerate(data) if target[i] != 1]

plt.scatter(class1_x, class1_y, c='r', marker='o')
plt.scatter(class2_x, class2_y, c='b', marker='x')

# plt.show()

linear_dataframe = pd.DataFrame()
linear_dataframe['x1'] = [x[0] for i, x in enumerate(data)]
linear_dataframe['x2'] = [x[1] for i, x in enumerate(data)]
linear_dataframe['target'] = target

# print(linear_dataframe)

my_feature_dataframe = linear_dataframe[["x1", "x2"]]
# print(my_feature_dataframe)

feature_columns = [tf.feature_column.numeric_column("x1"), tf.feature_column.numeric_column("x2")]

target_series = linear_dataframe["target"]

my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0001)

linear_regressor = tf.estimator.LinearRegressor(feature_columns=feature_columns, optimizer=my_optimizer)


def my_input_fn(feature_dataframe, target_series, batch_size=1, shuffle=True, num_epochs=None):
    features = {key: np.array(value) for key, value in dict(feature_dataframe).items()}

    ds = Dataset.from_tensor_slices((features, target_series))
    ds = ds.batch(batch_size).repeat(num_epochs)

    if shuffle:
        ds = ds.shuffle(buffer_size=10000)

    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels


_ = linear_regressor.train(input_fn=lambda: my_input_fn(my_feature_dataframe, target_series), steps=10000)

predict_input_fn = lambda: my_input_fn(my_feature_dataframe, target_series, num_epochs=1, shuffle=False)

predictions = linear_regressor.predict(input_fn=predict_input_fn)
predictions = np.array([item['predictions'][0] for item in predictions])

mean_squared_error = metrics.mean_squared_error(predictions, target_series)
root_mean_squared_error = math.sqrt(mean_squared_error)
# print("Mean Squared Error (on training data): %0.3f" % mean_squared_error)
print("Root Mean Squared Error (on training data): %0.3f" % root_mean_squared_error)

weight_1 = linear_regressor.get_variable_value('linear/linear_model/x1/weights')
weight_2 = linear_regressor.get_variable_value('linear/linear_model/x2/weights')
bias = linear_regressor.get_variable_value('linear/linear_model/bias_weights')
print('\n w1=%s w2=%s  bias=%s' % (weight_1, weight_2, bias))
[[_w1]] = weight_1
[[_w2]] = weight_2
[_b] = bias

# result_dataframe = pd.DataFrame()
# result_dataframe["predictions"] = pd.Series(predictions)
# result_dataframe["targets"] = target_series
linear_dataframe['predictions'] = predictions
# print('\nresult dataframe:\n%s' % linear_dataframe)

slope = -_w2 / _w1
y_intercept = _b / _w1

x1_series = linear_dataframe['x1']
best_fit = []
for i in x1_series:
    best_fit.append(slope * i + y_intercept)

plt.plot(x1_series, best_fit, 'g-')

plt.show()

kai.show_visualization_data(class1_x, class1_y, class2_x, class2_y
                            , [root_mean_squared_error, root_mean_squared_error]
                            , target_series, predictions
                            , 'blobs pandas linear regressor')
