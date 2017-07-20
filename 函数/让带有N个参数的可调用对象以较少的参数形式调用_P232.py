# -*- coding: utf-8 -*-
"""
functools.partial()
允许我们给一个或多个参数指定固定的值
"""
from functools import partial


def spam(a, b, c, d):
    print(a, b, c, d)

s1 = partial(spam, c=13)
s1(a=1, b=2, d=3)  # 1 2 13 3

s2 = partial(spam, a=42)
s2(b=1, c=2, d=3)  # 42 1 2 3


"""
例子,sort方法只能接受单参数的函数一起工作，因此与distance是不兼容的，用partical可以解决这个问题
"""
import math

points = [(3, 4), (1, 2), (7, 8), (5, 6)]


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)

pt = (4, 3)
points.sort(key=partial(distance, p2=pt))
print(points)  # [(3, 4), (1, 2), (5, 6), (7, 8)]
