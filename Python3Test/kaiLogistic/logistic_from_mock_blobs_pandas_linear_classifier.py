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
print('target=%s' % target)

class1_x = [x[0] for i, x in enumerate(data) if target[i] == 1]
class1_y = [x[1] for i, x in enumerate(data) if target[i] == 1]
class2_x = [x[0] for i, x in enumerate(data) if target[i] != 1]
class2_y = [x[1] for i, x in enumerate(data) if target[i] != 1]

# plt.figure(figsize=(8, 12))
# plt.scatter(class1_x, class1_y, c='r', marker='o')
# plt.scatter(class2_x, class2_y, c='b', marker='x')
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

my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.005)

linear_classifier = tf.estimator.LinearClassifier(feature_columns=feature_columns, optimizer=my_optimizer)


def my_input_fn(feature_dataframe, target_series, batch_size=1, shuffle=True, num_epochs=None):
    features = {key: np.array(value) for key, value in dict(feature_dataframe).items()}

    ds = Dataset.from_tensor_slices((features, target_series))
    ds = ds.batch(batch_size).repeat(num_epochs)

    if shuffle:
        ds = ds.shuffle(buffer_size=10000)

    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels


predict_input_fn = lambda: my_input_fn(my_feature_dataframe, target_series, num_epochs=1, shuffle=False)


def train_linear_regressor_model(steps, batch_size):
    periods = 10
    steps_per_period = steps / periods
    training_input_fn = lambda: my_input_fn(my_feature_dataframe, target_series, batch_size=batch_size)

    print("Training log losses model...")
    log_losses = []
    for period in range(0, periods):
        linear_classifier.train(input_fn=training_input_fn, steps=steps_per_period)
        probabilities = linear_classifier.predict(input_fn=predict_input_fn)
        probabilities = np.array([item['probabilities'][1] for item in probabilities])
        log_loss = metrics.log_loss(target_series, probabilities)
        print("  period %02d : %s" % (period, str(log_loss)))
        log_losses.append(log_loss)

    print("Model training finished.")

    # plt.figure()
    # plt.ylabel("LogLoss")
    # plt.xlabel("Periods")
    # plt.title("LogLoss vs. Periods")
    # plt.tight_layout()
    # plt.plot(log_losses, label="log_losses")
    # plt.legend()
    # plt.show()
    return log_losses


log_losses = train_linear_regressor_model(500, 10)

probabilities = linear_classifier.predict(input_fn=predict_input_fn)
probabilities = np.array([item['probabilities'][1] for item in probabilities])
linear_dataframe['probabilities'] = probabilities
print('\nresult dataframe:\n%s' % linear_dataframe)

weight_1 = linear_classifier.get_variable_value('linear/linear_model/x1/weights')
weight_2 = linear_classifier.get_variable_value('linear/linear_model/x2/weights')
bias = linear_classifier.get_variable_value('linear/linear_model/bias_weights')
print('\n w1=%s w2=%s  bias=%s' % (weight_1, weight_2, bias))
[[_w1]] = weight_1
[[_w2]] = weight_2
[_b] = bias

evaluation_metrics = linear_classifier.evaluate(input_fn=predict_input_fn)

print("\nAUC on the validation set: %0.2f" % evaluation_metrics['auc'])
print("Accuracy on the validation set: %0.2f" % evaluation_metrics['accuracy'])
# AUC 1.0   accuracy 1.0

# plt.figure()
# false_positive_rate, true_positive_rate, thresholds = metrics.roc_curve(
#     target_series, probabilities)
# plt.plot(false_positive_rate, true_positive_rate, label="our model")
# plt.plot([0, 1], [0, 1], label="random classifier")
# _ = plt.legend(loc=2)
# plt.show()

kai.show_visualization_data(class1_x, class1_y, class2_x, class2_y
                            , log_losses
                            , target_series, probabilities
                            , 'blobs pandas linear classifier')
