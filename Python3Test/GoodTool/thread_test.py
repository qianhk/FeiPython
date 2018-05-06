#!/usr/bin/env python3
# coding=utf-8

import sys
import time
import threading

# https://foofish.net/thread.html 为什么有人说 Python 多线程是鸡肋？
# gil 全局解释锁（Global Interpreter Lock)

print('sys.getcheckinterval() = %s' % sys.getcheckinterval())


def decrement(n):
    while n > 0:
        n -= 1


start = time.time()
decrement(1_0000_0000)
cost = time.time() - start

# mbp 2014版 cpu i7 6.07s
print('single thread: cost time = %s' % cost)

start = time.time()

t1 = threading.Thread(target=decrement, args=[5000_0000])
t2 = threading.Thread(target=decrement, args=[5000_0000])

t1.start()  # 启动线程，执行任务
t2.start()  # 同上

t1.join()  # 主线程阻塞，直到t1执行完成，主线程继续往后执行
t2.join()  # 同上

cost = time.time() - start
# mbp 2014版 cpu i7 6.65s
print('two thread: cost time = %s' % cost)
