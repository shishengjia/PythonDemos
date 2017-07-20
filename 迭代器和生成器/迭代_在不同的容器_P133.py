"""
chain()方法,接收多个输入
"""


from itertools import chain

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
c = [4, 5]

for x in chain(a, b, c):
    print(x, end=' ') # 1 2 3 4 x y z 4 5

"""
使用常规的加号可以将序列链接，但是局限于类型相同的序列，并且效率上也要比chain()差
"""
