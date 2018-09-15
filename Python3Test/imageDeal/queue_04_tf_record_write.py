#!/usr/bin/env python3
# coding=utf-8

import tensorflow as tf
import os

def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


num_shards = 2
instances_per_shard = 2

for i in range(num_shards):
    filename = f'../cache/imageDetal/data.tfrecords-{i}-of-{num_shards}'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    writer = tf.python_io.TFRecordWriter(filename)
    for j in range(instances_per_shard):
        example = tf.train.Example(features=tf.train.Features(feature={
            'i': _int64_feature(i),
            'j': _int64_feature(j)
        }))
        writer.write(example.SerializeToString())
    writer.close()
