#!/usr/bin/env python3
# coding=utf-8

import fire
import math


class Calculator(object):

    @staticmethod
    def double(number):
        return 2 * number


# ./testFire.py pi --n=100000
def pi(n):
    s = 0.0
    for i in range(n):
        s += 1.0 / (i + 1) / (i + 1)
    return math.sqrt(6 * s)


def fact(n):
    s = 1
    for i in range(n):
        s *= (i + 1)
    return s


if __name__ == '__main__':
    fire.Fire()  # ./testFire.py pi --n 100000  ./testFire.py pi 100000
    # fire.Fire(Calculator)  # ./testFire.py double --number 100
    # fire.Fire(fact)  # ./testFire.py --n 4
