
#最简单的方法，列表表达式
mylist = [1, 2, -1, -3, 4, -5]
print([x for x in mylist if x > 0])

#列表表达式在原始输入非常大的情况下会产生一个非常大的结果。这时可以考虑使用生成器表达式
pos = (x for x in mylist if x > 0)
for x in pos:
    print(x,end=',')

#如果筛选过程涉及异常或其他的一些复杂细节，可以使用filter()函数
values = ['1', '2', 'N/A', '3', '-']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
print(ivals)

# 用新值替换不满足条件的值
clip_neg = [x if x > 0 else 0 for x in mylist]
print(clip_neg)

"""
compress()函数
接受一个可迭代对象以及一个布尔选择器序列
输出所有在相应的布尔选择器中为True的可迭代对象元素
"""
from itertools import compress

address = [
    'N3 511',
    'N4 342',
    'N8 212',
    'N6 432',
    'N1 222',
]

counts = [7, 3, 6, 4, 8]
# 构造一个布尔选择器序列
more5 = [n > 5 for n in counts]
print(list(compress(address, more5)))
