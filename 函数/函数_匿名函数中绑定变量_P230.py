# -*- coding: utf-8 -*-

x = 10
a = lambda y: x + y

x = 20
b = lambda y: x + y

print(a(10), b(10))  # 30, 30

"""
原因是x是自由变量，在运行时才进行绑定而不是定义的时候绑定
所以lambda表达式中x的值应该是执行时确定的， 而此时x已经被再次赋值成为20
"""

"""
所以，希望匿名函数在定义时绑定变量，并且保持值不变，可以将那个值作为默认参数
"""

x = 10
a = lambda y, x=x: x + y

x = 20
b = lambda y, x=x: x + y
print(a(10), b(10))  # 20, 30


