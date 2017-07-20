# -*- coding: utf-8 -*-
"""
使用 * 开头的参数,接受任意数量的位置参数
"""


def avg(first, *rest):
    print(rest)
    return (first + sum(rest)) / (1 + len(rest))

avg(1, 2, 3, 4)  # (2, 3, 4) 可以看出rest是个元组

"""
使用 ** 开头的参数，接受任意数量的关键字参数
"""


def print_info(**kwargs):
    print(kwargs)

print_info(a=2, b=1)  # {'b': 1, 'a': 2}
print_info(**{'a': 1, 'b': 2})  # {'b': 2, 'a': 1}


