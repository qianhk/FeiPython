#!/usr/bin/env python3
# coding=utf-8

import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset
import math
import kaiLinear.line_from_linear_data_utils as kai

# https://colab.research.google.com/notebooks/mlcc/first_steps_with_tensor_flow.ipynb?hl=zh-cn#scrollTo=AZWF67uv0HTG

linear_dataframe = pd.read_csv("../data/linear_data.csv", sep=",")

print('linear_dataframe.describe()=%s\n' % linear_dataframe.describe())

x_series = linear_dataframe["x"].apply(lambda x: max(x, -10000))
my_feature_dataframe = linear_dataframe[["x"]]

x_feature_column = tf.feature_column.numeric_column("x")
feature_columns = [x_feature_column]

target_series = linear_dataframe["y"]

my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.0001)
# my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)

linear_regressor = tf.estimator.LinearRegressor(feature_columns=feature_columns, optimizer=my_optimizer)


def my_input_fn(feature_dataframe, target_series, batch_size=1, shuffle=True, num_epochs=None):
    features = {key: np.array(value) for key, value in dict(feature_dataframe).items()}

    ds = Dataset.from_tensor_slices((features, target_series))
    ds = ds.batch(batch_size).repeat(num_epochs)

    if shuffle:
        ds = ds.shuffle(buffer_size=10000)

    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels


_ = linear_regressor.train(input_fn=lambda: my_input_fn(my_feature_dataframe, target_series), steps=2000)

predict_input_fn = lambda: my_input_fn(my_feature_dataframe, target_series, num_epochs=1, shuffle=False)

predictions = linear_regressor.predict(input_fn=predict_input_fn)
predictions = np.array([item['predictions'][0] for item in predictions])

mean_squared_error = metrics.mean_squared_error(predictions, target_series)
root_mean_squared_error = math.sqrt(mean_squared_error)
print("Mean Squared Error (on training data): %0.3f" % mean_squared_error)
print("Root Mean Squared Error (on training data): %0.3f" % root_mean_squared_error)

min_y_value = target_series.min()
max_y_value = target_series.max()
min_max_difference = max_y_value - min_y_value

print("Min. x Value: %0.3f" % min_y_value)
print("Max. x: %0.3f" % max_y_value)
print("Difference between Min. and Max.: %0.3f" % min_max_difference)
print("Root Mean Squared Error: %0.3f" % root_mean_squared_error)

weight = linear_regressor.get_variable_value('linear/linear_model/x/weights')
bias = linear_regressor.get_variable_value('linear/linear_model/bias_weights')
print('\n weight=%s  bias=%s' % (weight, bias))
[[_w]] = weight
[_b] = bias

result_dataframe = pd.DataFrame()
result_dataframe["predictions"] = pd.Series(predictions)
result_dataframe["targets"] = target_series
print('\nresult dataframe:\n%s' % result_dataframe.describe())

kai.show_visualization_data(x_series, target_series, _w, _b, None, title='Pandas')
