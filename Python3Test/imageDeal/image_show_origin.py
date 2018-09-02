#!/usr/bin/env python3
# coding=utf-8

import matplotlib.pyplot as plt
import tensorflow as tf

jpgFile = tf.gfile.FastGFile('../data/cat.jpg', 'rb')
image_raw_data = jpgFile.read()

dest_dir = '../logs/imageDeal/'

with tf.Session() as sess:
    image_data = tf.image.decode_jpeg(image_raw_data)
    image_data_eval = image_data.eval()
    # print(image_data_eval)
    # original image_data_eval.shape=(1797, 2673, 3) <dtype: 'uint8'> [162 161 140]
    print(f'original image_data_eval.shape={image_data_eval.shape} {image_data.dtype} {image_data_eval[0, 0]}')  # (1797, 2673, 3)
    plt.imshow(image_data_eval)
    plt.title(f'image_data_eval {image_data_eval.shape} {image_data.dtype} {image_data_eval[0, 0]}')
    plt.show()

    image_data_type_float32 = tf.image.convert_image_dtype(image_data, dtype=tf.float32)
    image_data_type_float32_eval = image_data_type_float32.eval()
    # float32_eval.shape=(1797, 2673, 3) float32 [ 0.63529414  0.63137257  0.54901963]
    print(f'float32_eval.shape={image_data_type_float32_eval.shape}'
          f' {image_data_type_float32_eval.dtype} {image_data_type_float32_eval[0, 0]}')  # (1797, 2673, 3)
    plt.imshow(image_data_type_float32_eval)
    plt.title(f'float32_eval {image_data_type_float32_eval.shape} {image_data_type_float32_eval.dtype}'
              f' {image_data_type_float32_eval[0, 0]}')
    plt.show()

    # encoded_image = tf.image.encode_png(image_data, compression=3)  # encode必须用uint8 ，不然全黑
    encoded_image = tf.image.encode_jpeg(image_data, quality=None)  # encode必须用uint8 ，不然报错
    encoded_image_eval = encoded_image.eval()
    with tf.gfile.GFile(dest_dir + 'cat_compression.jpg', 'wb') as f:
        f.write(encoded_image.eval())

    # resize_300_300_image = tf.image.resize_images(image_data, [300, 300], method=0)
    # print(f'resize_300_300_image shape={resize_300_300_image.get_shape()}')
    # resize_300_300_image_eval = resize_300_300_image.eval()
    # print(f'resize_300_300_image_eval.shape={resize_300_300_image_eval.shape}')
    # plt.imshow(resize_300_300_image_eval)
    # plt.title('resize_300_300_image_eval')
    # plt.show()

    # encoded_image = tf.image.encode_jpeg(resized)
    # encoded_image = tf.image.encode_jpeg(tf.image.convert_image_dtype(resized, dtype=tf.uint8))
    # with tf.gfile.GFile(dest_dir + 'cat_300_300.jpg', 'wb') as f:
    #     f.write(encoded_image.eval())
