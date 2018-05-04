#!/usr/bin/env python
# coding=utf-8

import tfcoreml as tf_converter

tf_converter.convert(tf_model_path='./pb/kai_linear_only_mul.pb',
                     mlmodel_path='./kai_linear_only_mul.mlmodel',
                     output_feature_names=['calcY:0'])
