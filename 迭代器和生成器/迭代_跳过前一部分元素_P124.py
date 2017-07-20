"""
第一种方法使用dropwhile()函数
需要注意该函数一旦遇到某个元素不满足测试要求，那么之后的所有元素就会不经过筛选而直接返回
所以下面的例子中文章中间的注释并没有被丢弃
"""
from itertools import dropwhile

with open('../test.txt') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')


"""
output
Man:what's your name
B:where are you form
>>>>>>>>>>>>>>>>>>>>>>>>>
Man:The question is
Python is powerful
# help
I like Python
It's interesting
"""

"""
第二种方法，如果恰好知道要跳过几个元素，那么可以使用islice()函数
"""
from itertools import islice

x = [1, 2, 3, 'a', 'b', 'c']
for x in islice(x, 3, None): # None表示后面所有元素都包括进来
    print(x, end=' ') # a b c
