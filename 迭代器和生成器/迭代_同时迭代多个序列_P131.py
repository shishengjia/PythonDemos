"""
zip函数
可以接受多余2个的序列，一般不常见
需要注意的是zip()创建的只是一个迭代器
"""
x = [1, 2, 3]
y = [4, 5, 6]
for item in zip(x, y):
    print(item)
"""
(1, 4)
(2, 5)
(3, 6)
"""

"""
整个迭代的长度取决于最短的输入序列
"""
x = [1, 2, 3]
y = [4, 5, 6, 7, 8]

for item in zip(x, y):
    print(item)

"""
(1, 4)
(2, 5)
(3, 6)
"""

"""
不希望出现上面的情况，可以使用itertools.zip_longest()
"""
from itertools import zip_longest

x = [1, 2, 3]
y = [4, 5, 6, 7, 8]

for item in zip_longest(x, y):
    print(item)

"""
(1, 4)
(2, 5)
(3, 6)
(None, 7)
(None, 8)
"""
