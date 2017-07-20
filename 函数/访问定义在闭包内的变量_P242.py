# -*- coding: utf-8 -*-

"""
通过编写存取函数并将它们作为函数属性附加到闭包上来提供对内层变量的访问支持
"""


def sample():
    n = 0

    def func():
        print('n=', n)

    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # 讲存取函数以直接的方式附加到闭包函数上
    func.get_n = get_n
    func.set_n = set_n

    return func

f = sample()
print(f())

f.set_n(10)
print(f())

print(f.get_n())