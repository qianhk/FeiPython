#!/usr/bin/python
# coding=utf-8

import sys
from math import *
from math import sqrt
import os



def add_number(a, b=1):
    '''Print add number

    The two number add
    :param a: a
    :param b: b
    :return: return
    '''
    print ('add two number {} + {} = {}'.format(a, b, a + b))


add_number(1, 2)

add_number(13, 18)

add_number(14)

add_number(b=2, a=3)


def total(a=5, *numbers, **phonebook):
    print('a:', a)  # python2 output: ('a:', 10)     python3 output:a: 10

    for singleItem in numbers:
        print ('single item:', singleItem)

    for first, second in phonebook.items():
        print (first, second)  # python3 right,  python2 order error


print (total(10, 1, 2, 3, jack=123, john=456, kai=789))

print(add_number.__doc__)

# help(add_number)

print ('The command line argument are: ')
for i in sys.argv:
    print (i)

print ('\nThe Python Path is: ')
for path in sys.path:
    print(path)


print ('Square root of 16 is', sqrt(16), pow(5, 2))

if __name__ == '__main__':
    print ('This program is being run by itself')
else:
    print ('I am being imported from another module', __name__)

__version__ = '0.0.2'

kai = 'kai-0.0.1'

print (dir(sys))

print ('sys.api_version', sys.api_version)
print ('sys.version', sys.version, sys.version_info)

print ('os.getcwd', os.getcwd())


