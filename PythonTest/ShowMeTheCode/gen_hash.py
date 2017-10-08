#!/usr/bin/env python
# coding=utf-8

__author__ = 'Abcdefg'

import hashlib
from collections import defaultdict

try:
    input = raw_input
except:
    pass

db = {}
db = defaultdict(lambda: 'N/A')  # 去掉登录可能产生的KeyError


def get_md5(password):
    a = hashlib.md5()
    a.update(password.encode('utf-8'))
    return a.hexdigest()


def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')


def login(username, password):
    b = get_md5(password + username + 'the-Salt')
    if b == db[username]:
        return True
    else:
        return False


a = input('注册输入用户名：')
b = input('注册输入密码：')
register(a, b)
a = input('登录输入用户名：')
b = input('登录输入密码：')
print(login(a, b))
