#!/usr/bin/env python
# coding=utf-8

import os
from PIL import Image


def process_image(filename, mwidth=640, mheight=1136):
    image = Image.open(filename)
    w, h = image.size
    if w <= mwidth and h <= mheight:
        print(filename, 'is OK.')
        return
    if 1.0 * w / mwidth > 1.0 * h / mheight:
        scale = 1.0 * w / mwidth
        new_im = image.resize((int(w / scale), int(h / scale)), Image.ANTIALIAS)
    else:
        scale = 1.0 * h / mheight
        new_im = image.resize((int(w / scale), int(h / scale)), Image.ANTIALIAS)
    new_im.save('../cache/new-' + filename)
    new_im.close()


if __name__ == '__main__':
    ext = ['jpg', 'jpeg', 'png']
    files = os.listdir('.')
    for file in files:
        if file.split('.')[-1] in ext:
            process_image(file)
