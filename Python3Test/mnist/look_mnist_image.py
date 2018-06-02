#!/usr/bin/env python3
# coding=utf-8


# code from http://www.ciphermagic.cn/mnist-transform.html

import struct
import numpy as np
from PIL import Image
import os
import shutil


# 转换图片
def read_image(file_name, dir_name, out_file_name, num=-1):
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    os.makedirs(dir_name)
    # 二进制的形式读入
    filename = file_name
    binfile = open(filename, 'rb')
    buf = binfile.read()
    # 大端法读入 4 个 unsigned int32
    # struct 用法参见网站 http://www.cnblogs.com/gala/archive/2011/09/22/2184801.html
    index = 0
    magic, num_images, num_rows, num_columns = struct.unpack_from('>IIII', buf, index)
    index += struct.calcsize('>IIII')
    num_images = num_images if num == -1 else num
    # 将每张图片按照格式存储到对应位置
    for image in range(0, num_images):
        im = struct.unpack_from('>784B', buf, index)
        index += struct.calcsize('>784B')
        # 这里注意 Image 对象的 dtype 是 uint8，需要转换
        im = np.array(im, dtype='uint8')
        im = im.reshape(28, 28)
        im = Image.fromarray(im)
        im.save('%s/%s_%s.bmp' % (dir_name, out_file_name, image), 'bmp')


# 转换 label
def read_label(filename, save_filename):
    f = open(filename, 'rb')
    index = 0
    buf = f.read()
    f.close()
    magic, labels = struct.unpack_from('>II', buf, index)
    index += struct.calcsize('>II')
    label_arr = [0] * labels
    for x in range(0, labels):
        label_arr[x] = int(struct.unpack_from('>B', buf, index)[0])
        index += struct.calcsize('>B')
    save = open(save_filename, 'w')
    save.write(','.join(map(lambda n: str(n), label_arr)))
    save.write('\n')
    save.close()
    print('save labels success')


if __name__ == '__main__':
    # read_image('../cache/mnist/t10k-images-idx3-ubyte', '../logs/mnist/test', 'test', 20)
    read_image('../cache/mnist/train-images-idx3-ubyte', '../logs/mnist/train', 'train', 20)
    # read_label('../cache/mnist/t10k-labels-idx1-ubyte', '../logs/mnist/test_labels.txt')
    read_label('../cache/mnist/train-labels-idx1-ubyte', '../logs/mnist/train_labels.txt')
    pass
