#!/usr/bin/env python3
# coding=utf-8

import pandas as pd

# from https://colab.research.google.com/notebooks/mlcc/intro_to_pandas.ipynb?hl=zh-cn

print('\npandas version = %s' % (pd.__version__))

series = pd.Series(['KaiKai', 'YangYang', 'ChunChun'])

print('\nseries =\n%s  type=%s' % (series, type(series)))

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento', 'TaiZhou'])
population = pd.Series([852469, 1015785, 485199])  # using NaN instead

dataFrame = pd.DataFrame({'City name': city_names, 'Population': population})

print('\ndataFrame=\n%s' % dataFrame)

california_housing_dataframe = pd.read_csv("../cache/california_housing_train.csv", sep=",")
describe = california_housing_dataframe.describe()

print('\ncalifornia_housing_dataframe describe=\n%s' % describe)

# will print all record
# print('\ncalifornia_housing_dataframe=\n%s' % california_housing_dataframe)

print('\ncalifornia_housing_dataframe head()=\n%s' % california_housing_dataframe.head(10))

# california_housing_dataframe.hist('housing_median_age')

print('\ncalifornia_housing_dataframe.hist(\'housing_median_age\') = \n%s' % california_housing_dataframe.hist(
    'housing_median_age'))

cityNames = dataFrame['City name']
print('\ncityNames type=%s value =\n%s' % (type(cityNames), cityNames))

cityNames_sub1 = cityNames[1]
print('\ncityNames[1] type=%s value=%s' % (type(cityNames_sub1), cityNames_sub1))

dataFrame02 = dataFrame[0:2]
print('\ndataFrame02 type=%s value=\n%s' % (type(dataFrame02), dataFrame02))
