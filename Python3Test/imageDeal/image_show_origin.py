#!/usr/bin/env python3
# coding=utf-8

import matplotlib.pyplot as plt
import tensorflow as tf

jpgFile = tf.gfile.FastGFile('../data/cat.jpg', 'rb')
image_raw_data = jpgFile.read()

dest_dir = '../logs/imageDeal/'


def resize_300(p_image_data_float32, method, file_suffix):
    _resize_300_300_image = tf.image.resize_images(p_image_data_float32, [300, 300], method=method)
    _resize_300_300_image_uint8 = tf.image.convert_image_dtype(_resize_300_300_image, dtype=tf.uint8)
    _encoded_image = tf.image.encode_jpeg(_resize_300_300_image_uint8, quality=None)
    with tf.gfile.GFile(f'{dest_dir}/cat_300_300_{file_suffix}.jpg', 'wb') as _f:
        _f.write(_encoded_image.eval())


with tf.Session() as sess:
    image_data = tf.image.decode_jpeg(image_raw_data)
    image_data_eval = image_data.eval()
    # print(image_data_eval)
    # original image_data_eval.shape=(1797, 2673, 3) <dtype: 'uint8'> [162 161 140]
    print(f'original image_data_eval.shape={image_data_eval.shape} {image_data.dtype} {image_data_eval[0, 0]}')  # (1797, 2673, 3)
    # plt.imshow(image_data_eval)
    # plt.title(f'image_data_eval {image_data_eval.shape} {image_data.dtype} {image_data_eval[0, 0]}')
    # plt.show()

    image_data_type_float32 = tf.image.convert_image_dtype(image_data, dtype=tf.float32)
    image_data_type_float32_eval = image_data_type_float32.eval()
    # float32_eval.shape=(1797, 2673, 3) float32 [ 0.63529414  0.63137257  0.54901963]
    print(f'float32_eval.shape={image_data_type_float32_eval.shape}'
          f' {image_data_type_float32_eval.dtype} {image_data_type_float32_eval[0, 0]}')  # (1797, 2673, 3)
    # plt.imshow(image_data_type_float32_eval)
    # plt.title(f'float32_eval {image_data_type_float32_eval.shape} {image_data_type_float32_eval.dtype}'
    #           f' {image_data_type_float32_eval[0, 0]}')
    # plt.show()

    # encoded_image = tf.image.encode_png(image_data, compression=3)  # encode必须用uint8 ，不然全黑或者报错
    encoded_image = tf.image.encode_jpeg(image_data, quality=None)  # encode必须用uint8 ，不然全黑或者报错
    encoded_image_eval = encoded_image.eval()
    with tf.gfile.GFile(dest_dir + 'cat_compression.jpg', 'wb') as f:
        f.write(encoded_image.eval())

    # 以下调整图片大小
    resize_300_300_image = tf.image.resize_images(image_data_type_float32, [300, 300], method=0)
    print(f'resize_300_300_image shape={resize_300_300_image.get_shape()}')
    resize_300_300_image_eval = resize_300_300_image.eval()
    print(f'resize_300_300_image_eval.shape={resize_300_300_image_eval.shape}')
    # plt.imshow(resize_300_300_image_eval)
    # plt.title(f'resize_300 {resize_300_300_image_eval.shape} {resize_300_300_image_eval.dtype} {resize_300_300_image_eval[0, 0]}')
    # plt.show()

    resize_300_300_image_uint8 = tf.image.convert_image_dtype(resize_300_300_image, dtype=tf.uint8)
    encoded_image = tf.image.encode_jpeg(resize_300_300_image_uint8, quality=None)
    with tf.gfile.GFile(dest_dir + 'cat_300_300_BILINEAR.jpg', 'wb') as f:
        f.write(encoded_image.eval())

    resize_300(image_data_type_float32, 1, 'NEAREST')
    resize_300(image_data_type_float32, 2, 'BICUBIC')
    resize_300(image_data_type_float32, 3, 'AREA')

    (origin_height, origin_width, origin_channel) = image_data_type_float32_eval.shape

    resize_width = 800
    resize_height = round(origin_height * resize_width / origin_width)

    resize_image = tf.image.resize_images(image_data_type_float32, [resize_height, resize_width], method=1)
    resize_image_uint8 = tf.image.convert_image_dtype(resize_image, dtype=tf.uint8)
    encoded_image = tf.image.encode_jpeg(resize_image_uint8, quality=None)
    with tf.gfile.GFile(f'{dest_dir}/cat_{resize_width}_{resize_height}.jpg', 'wb') as f:
        f.write(encoded_image.eval())

    plt.imshow(resize_image_uint8.eval())
    plt.title(f'resize_image {resize_width}*{resize_height}')
    plt.show()

    # 以下图片翻转
    flipped = tf.image.flip_up_down(resize_image)
    flipped2 = tf.image.flip_left_right(resize_image)
    flipped3 = tf.image.transpose_image(resize_image)

    plt.figure()
    plt.title('up_down left_right transpose')  # 多子图为啥不显示整体标题

    subplot_label_y = -10

    ax = plt.subplot(221)
    ax.text(0, subplot_label_y, 'origin')
    ax.imshow(resize_image_uint8.eval())

    ax = plt.subplot(222)
    ax.text(0, subplot_label_y, 'up_down')
    ax.imshow(tf.image.convert_image_dtype(flipped, dtype=tf.uint8).eval())

    ax = plt.subplot(223)
    ax.text(0, subplot_label_y, 'left_right')
    ax.imshow(tf.image.convert_image_dtype(flipped2, dtype=tf.uint8).eval())

    ax = plt.subplot(224)
    ax.text(0, subplot_label_y, 'transpose')
    ax.imshow(tf.image.convert_image_dtype(flipped3, dtype=tf.uint8).eval())

    plt.show()

    # 以下图像色彩调整
    adjusted = tf.image.adjust_brightness(resize_image, -0.5)
    adjusted2 = tf.image.adjust_brightness(resize_image, +0.5)

    plt.figure()
    plt.figure(figsize=(15, 30))

    ax = plt.subplot(521)
    ax.imshow(tf.image.convert_image_dtype(adjusted, dtype=tf.uint8).eval())
    ax.text(0, subplot_label_y, 'brightness -0.5')

    ax = plt.subplot(522)
    ax.imshow(tf.image.convert_image_dtype(adjusted2, dtype=tf.uint8).eval())
    ax.text(0, subplot_label_y, 'brightness +0.5')

    ax = plt.subplot(523)
    ax.imshow(tf.image.convert_image_dtype(tf.image.adjust_contrast(resize_image, -5), dtype=tf.uint8).eval())
    ax.text(0, subplot_label_y, 'contrast -5')

    ax = plt.subplot(524)
    ax.imshow(tf.image.convert_image_dtype(tf.image.adjust_contrast(resize_image, +5), dtype=tf.uint8).eval())
    ax.text(0, subplot_label_y, 'contrast +5')

    ax = plt.subplot(525)
    ax.imshow(tf.image.convert_image_dtype(tf.image.adjust_hue(resize_image, 0.2), dtype=tf.uint8).eval())
    ax.text(0, subplot_label_y, 'hue +0.2')

    ax = plt.subplot(526)
    ax.imshow(tf.image.convert_image_dtype(tf.image.adjust_hue(resize_image, 0.6), dtype=tf.uint8).eval())
    ax.text(0, subplot_label_y, 'hue +0.6')

    ax = plt.subplot(527)
    ax.imshow(tf.image.convert_image_dtype(tf.image.adjust_saturation(resize_image, -5), dtype=tf.uint8).eval())
    ax.text(0, subplot_label_y, 'saturation -5')

    ax = plt.subplot(528)
    ax.imshow(tf.image.convert_image_dtype(tf.image.adjust_saturation(resize_image, 5), dtype=tf.uint8).eval())
    ax.text(0, subplot_label_y, 'saturation +5')

    ax = plt.subplot(529)
    ax.text(0, subplot_label_y, 'origin')
    ax.imshow(resize_image_uint8.eval())

    ax = plt.subplot(5, 2, 10)
    ax.imshow(tf.image.convert_image_dtype(tf.image.per_image_standardization(resize_image), dtype=tf.uint8).eval())
    ax.text(0, subplot_label_y, 'standardization')

    plt.show()
