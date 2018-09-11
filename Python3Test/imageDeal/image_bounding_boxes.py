#!/usr/bin/env python3
# coding=utf-8

import matplotlib.pyplot as plt
import tensorflow as tf

jpgFile = tf.gfile.FastGFile('../data/cat.jpg', 'rb')
image_raw_data = jpgFile.read()

dest_dir = '../logs/imageDeal/'

with tf.Session() as sess:
    image_data = tf.image.decode_jpeg(image_raw_data)
    image_data = tf.image.convert_image_dtype(image_data, tf.float32)

    (origin_height, origin_width, origin_channel) = image_data.eval().shape
    print(f'origin_height={origin_height} origin_width={origin_width} origin_channel={origin_channel}')

    resize_width = 400
    resize_height = round(origin_height * resize_width / origin_width)
    resize_image = tf.image.resize_images(image_data, [resize_height, resize_width], method=1)

    boxes = tf.constant([[[0.05, 0.05, 0.9, 0.7], [0.35, 0.47, 0.5, 0.56]]])
    resize_image_shape = tf.shape(resize_image)
    print(f'resize_image_shape={resize_image_shape.eval()}')
    begin, size, bbox_for_draw = tf.image.sample_distorted_bounding_box(
        resize_image_shape, bounding_boxes=boxes, min_object_covered=0.4)
    print(f'after sample_distorted_bounding_box: begin={begin.eval()} size={size.eval()} bbox_for_draw={bbox_for_draw.eval()}')

    distorted_image = tf.slice(resize_image, begin, size)
    plt.imshow(distorted_image.eval())
    plt.show()

    batched_image = tf.expand_dims(resize_image, 0)
    image_with_box = tf.image.draw_bounding_boxes(batched_image, boxes)

    plt.figure()
    # ax = plt.subplot(121)
    # plt.imshow(result.eval())
    plt.imshow(image_with_box[0].eval())
    plt.show()

    encoded_image = tf.image.encode_jpeg(tf.image.convert_image_dtype(image_with_box[0], tf.uint8), quality=None)
    with tf.gfile.GFile(dest_dir + 'cat_bounding_boxes.jpg', 'wb') as f:
        f.write(encoded_image.eval())
