#!/usr/bin/env python3
# coding=utf-8


class Proxy(object):

    def __init__(self, target):
        self.target = target

    #
    # 注意在获取target对象时，不能直接使用self.target，因为self.target会再次调用__getattribute__方法，
    # 这样就会导致死循环致堆栈过深曝出异常。取而代之应该使用object.__getattribute__方法来获取对象的属性值。
    #
    def __getattribute__(self, name):
        target = object.__getattribute__(self, "target")
        attr = object.__getattribute__(target, name)

        if name == 'print_str':
            def new_attr(*args, **kwargs):  # 包装
                print("before print")
                res = attr(*args, **kwargs)
                print("after print")
                return res

            return new_attr
        else:
            return attr


class RealHello(object):

    @staticmethod
    def print_str(s):
        print('hello %s' % s)

    @staticmethod
    def print_str2(s):
        print('hello2 %s' % s)


if __name__ == '__main__':
    t = RealHello()
    p = Proxy(t)
    p.print_str("world")
    p.print_str2("world")
