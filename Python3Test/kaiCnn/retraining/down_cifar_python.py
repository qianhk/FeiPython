#!/usr/bin/env python3
# coding=utf-8

import os
import tarfile
import shutil
import urllib.request
import numpy as np
import _pickle as cPickle
import scipy.misc

cache_dir = '../../cache/'
extract_folder = os.path.join(cache_dir, 'cifar-10-batches-py')

if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

down_url = 'http://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz'
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

need_files_set = set([f'data_batch_{i}' for i in range(1, 6)])
need_files_set.add('batches.meta')
need_files_set.add('test_batch')

# print(extract_files_set)
# print(need_files_set)

intersection_set = extract_files_set.intersection(need_files_set)
# print(intersection_set)

if len(intersection_set) < len(need_files_set):
    if os.path.exists(extract_folder):
        shutil.rmtree(extract_folder)
    tar = tarfile.open(file_path, 'r:gz')
    tar.extractall(cache_dir)
    tar.close()
    print(f'extractall to {cache_dir} success.')

objects = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']


def load_batch_from_file(file):
    file_conn = open(file, 'rb')
    _image_dict = cPickle.load(file_conn, encoding='latin1')
    file_conn.close()
    return _image_dict


def save_images_from_dict(_image_dict, _folder):
    _labels = _image_dict['labels']
    _filenames = _image_dict['filenames']
    _data = image_dict['data']
    for ix, label in enumerate(_labels):
        _folder_path = os.path.join(_folder, objects[label])
        _filename = _filenames[ix]
        _image_array = _data[ix]
        _image_array.resize([3, 32, 32])
        # _image_array2 = _image_array.transpose()
        _image_array3 = _image_array.transpose([1, 2, 0])
        output_location = os.path.join(_folder_path, _filename)
        scipy.misc.imsave(output_location, _image_array3)


train_folder = os.path.join(extract_folder, 'train_dir')
train_names = ['data_batch_' + str(x) for x in range(1, 6)]
if not os.path.isdir(train_folder):
    for i in range(len(objects)):
        folder = os.path.join(train_folder, objects[i])
        os.makedirs(folder)
    for file in train_names:
        print(f'Saving images from file: {file}')
        file_location = os.path.join(extract_folder, file)
        image_dict = load_batch_from_file(file_location)
        save_images_from_dict(image_dict, train_folder)

test_folder = os.path.join(extract_folder, 'validation_dir')
test_names = ['test_Batch']
if not os.path.isdir(test_folder):
    for i in range(len(objects)):
        folder = os.path.join(test_folder, objects[i])
        os.makedirs(folder)
    for file in test_names:
        print(f'Saving images from file: {file}')
        file_location = os.path.join(extract_folder, file)
        image_dict = load_batch_from_file(file_location)
        save_images_from_dict(image_dict, test_folder)

cifar_labels_file = os.path.join(extract_folder, 'cifar10_labels.txt')
if not os.path.exists(cifar_labels_file):
    print(f'Write labels file, {cifar_labels_file}')
    with open(cifar_labels_file, 'w') as labels_file:
        for item in objects:
            labels_file.write(f'{item}\n')
