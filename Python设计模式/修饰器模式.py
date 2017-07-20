# -*- coding: utf-8 -*-
from timeit import Timer


"""
求斐波那契数列，最朴素的实现，效率非常低，在本机上将近18秒才执行完
"""


def fibonacci(n):
    assert (n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n-1) + fibonacci(n-2)

# if __name__ == '__main__':
#     t = Timer('fibonacci(8)', 'from __main__ import fibonacci')
#     print(t.timeit())



"""
下面是用dict来存储斐波那契数列中已经计算好的数值，提升速度,仅仅只需0.2秒多
"""
known = {0: 0, 1: 1}


def fibonacci_2(n):
    assert (n >= 0), 'n must be >= 0'
    if n in known:
        return n
    res = fibonacci_2(n-1) + fibonacci_2(n-2)
    known[n] = res
    return res

if __name__ == '__main__':
    t = Timer('fibonacci_2(8)', 'from __main__ import fibonacci_2')
    print(t.timeit())


"""
但是上面的例子，虽然性能提升了，但是代码不够简洁，将来继续扩展该函数的时候，代码将更加复杂
下面是用修饰器模式
"""


import functools


def memoize(fn):
    known = dict()

    @functools.wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]

    return memoizer

