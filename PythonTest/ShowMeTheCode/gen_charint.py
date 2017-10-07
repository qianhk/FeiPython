#!/usr/bin/env python
# coding=utf-8

import random
import string


def gen_charint(filename, width = 4, num = 200):
    f = open(filename, 'wb')
    charint = string.digits + string.letters
    for i in range(num):
        verify = [random.choice(charint) for j in range(width)]
        verify = ''.join(verify) + '\n'
        f.write(verify)
    f.close()

if __name__ == '__main__':

    filename = 'result.txt'
    width = 8
    num = 200
    gen_charint(filename, width, num)




