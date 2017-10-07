#!/usr/bin/env python
# coding=utf-8

from PIL import Image, ImageDraw, ImageFont
import sys


def image_addnum(image_name, num):
    im = Image.open(image_name)
    draw = ImageDraw.Draw(im)

    w = im.width
    h = im.height
    print ('fp={} size={} format={} mode={}'.format(image_name, im.size, im.format, im.mode))

    # im.show()

    # font = ImageFont.load_default()
    # font.size = int(h * 0.5)
    font = ImageFont.truetype('Arial.ttf', size=int(h * 0.2))

    draw.text((w * 0.8, h * 0.05), num, font=font, fill=(255, 0, 0, 128))
    split = image_name.split('.')
    im.save('../cache/' + split[0] + '2.' + split[1])


if __name__ == '__main__':
    print ('sys.platform', sys.platform)
    image_addnum('panda.jpg', '3')
