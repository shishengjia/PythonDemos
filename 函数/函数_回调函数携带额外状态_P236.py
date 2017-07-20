# -*- coding: utf-8 -*-
from functools import reduce


def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)


def add(*args):
    return reduce(lambda x,y: x + y, args)

"""
1.使用绑定方法
下面的类保存一个内部的序列号，每收到一个结果就递增
"""


class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))

r = ResultHandler()
apply_async(add, (1, 2, 3), callback=r.handler)  # [1] Got: 6
apply_async(add, (1, 2), callback=r.handler)  # [2] Got: 3


"""
2.使用闭包
"""


def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

    return handler

handler = make_handler()
apply_async(add, (1, 2, 3), callback=handler)  # [1] Got: 6
apply_async(add, (1, 2), callback=handler)  # [2] Got: 3

"""
3.使用协程
"""
