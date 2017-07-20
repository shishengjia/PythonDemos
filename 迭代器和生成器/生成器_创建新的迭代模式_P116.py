"""
实现新的迭代模式，可使用生成器函数来定义
"""

def frange(start, stop, increment=0.1):
    x = start
    while x < stop:
        yield x
        x += increment

"""
注意，由于浮点数的问题，实际输出可能与预想的不一样
"""
for n in frange(1, 2, 0.5):
    print(n)
