#!/usr/bin/env python3
# coding=utf-8

import os
import tarfile
import shutil
from six.moves import urllib

cache_dir = '../../cache/'
extract_folder = os.path.join(cache_dir, 'cifar-10-batches-bin')

if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

down_url = 'http://www.cs.toronto.edu/~kriz/cifar-10-binary.tar.gz'
# down_url = 'http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz'
# down_url = 'http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz'
filename = down_url.split('/')[-1]
file_path = os.path.join(cache_dir, filename)


def _recall_func(num, block_size, total_size):
    down_size = num * block_size
    down_size_kb = total_size / 1024
    if total_size > 0:
        if down_size > total_size:
            down_size = total_size
        print('\r>> downloading %s totalSize=%.1fKB %.1f%%' % (
            filename, down_size_kb, down_size / total_size * 100.0))
    else:
        print('\r>> downloading %s,  downloaded size=%.2fKb' % (filename, down_size_kb))


if not os.path.isfile(file_path):
    tmp_file_path = file_path + '.tmp'
    _file_path, _headers = urllib.request.urlretrieve(down_url, tmp_file_path, _recall_func)
    # print(f'fp={_file_path} headers=\n{_headers}') # _file_path等同tmp_file_path _header是响应头
    os.rename(tmp_file_path, file_path)
    file_info = os.stat(file_path)
    print('Successfully download', file_path, file_info.st_size, 'bytes')

if os.path.exists(extract_folder):
    extract_files_set = set(os.listdir(extract_folder))
else:
    extract_files_set = set()

need_files_set = {'data_batch_1.bin', 'data_batch_2.bin', 'data_batch_3.bin', 'data_batch_4.bin', 'data_batch_5.bin', 'test_batch.bin'}
# print(extract_files_set)
# print(need_files_set)
intersection_set = extract_files_set.intersection(need_files_set)
# print(intersection_set)

if len(intersection_set) < len(need_files_set):
    if os.path.exists(extract_folder):
        shutil.rmtree(extract_folder)
    tarfile.open(file_path, 'r:gz').extractall(cache_dir)
    print(f'extractall to {cache_dir} success.')
