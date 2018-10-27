#!/usr/bin/env python3
# coding=utf-8

import os
import tarfile
from six.moves import urllib

extract_folder = '../../cache/cifar-10-batches-bin'

data_dir = 'temp'

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

cifar10_url = 'http://www.cs.toronto.edu/~kriz/cifar-10-binary.tar.gz'
data_file = os.path.join(data_dir, 'cifar-10-binary.tar.gz')

if not os.path.isfile(data_file):
    filePath, _ = urllib.request.urlretrieve(cifar10_url, data_file)
    tarfile.open(filePath, 'r:gz').extractall(data_dir)
