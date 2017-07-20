# -*- coding: utf-8 -*-
"""
默认参数的值应该总是不可变对象，像列表子类的容器是不可选的
对默认参数的赋值只会在函数定义的时候绑定一次
"""

"""
最基本的用法
"""


def spam(a, b=3):
    pass


"""
如果默认值是可变容器，例如列表，集合或者字典，应该把None作为默认值
"""


def spam_0(a, b=None):
    if b is None:
        b = []


"""
可能会犯以下错误，下面给出的示例在检测某些也定输入是也会判定为False
"""


def spam_1(a, b=None):
    if not b:
        b = []
    print(b)

spam_1(1)  # []
x = []
spam_1(1, x)  # []
spam_1(1, 0)  # []
spam_1(1, '')  # []

"""
如果不想提供默认值，只想检测可选参数是否被赋予了某个特定的值
注意区分不传递任何值和传递None之间的区别
"""
_no_value = object()


def spam_2(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')

spam_2(1)  # No b balue supplied
spam_2(1, 2)  # b = 2
spam_2(1, None)  # b = None



