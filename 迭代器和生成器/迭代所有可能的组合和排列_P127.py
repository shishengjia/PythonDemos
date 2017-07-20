"""
第一种，使用itertools.permutations()
在乎顺序，且选择过的元素之后将不在考虑范围内
"""
from itertools import permutations

items = ['a', 'b', 'c']
for p in permutations(items):
    print(p)

"""
output
('a', 'b', 'c')
('a', 'c', 'b')
('b', 'a', 'c')
('b', 'c', 'a')
('c', 'a', 'b')
('c', 'b', 'a')
"""

# 想得到较短长度的全排列
for p in permutations(items, 2):
    print(p)

"""
output
('a', 'b')
('a', 'c')
('b', 'a')
('b', 'c')
('c', 'a')
('c', 'b')
"""

"""
第二种，使用itertools.combinations()函数
选择过的元素之后将不在考虑范围内，且不考虑顺序问题
"""
from itertools import combinations

for p in combinations(items, 3):
    print(p)

"""
output
('a', 'b', 'c')
"""

for p in combinations(items, 2):
    print(p)

"""
output
('a', 'b')
('a', 'c')
('b', 'c')
"""

"""
上面两种方法，被选择过的元素将从考虑范围内删去
使用itertools.combinations_with_replacement函数可以解除这一限制
"""
from itertools import combinations_with_replacement

for p in combinations_with_replacement(items, 3):
    print(p)

"""
output
('a', 'a', 'a')
('a', 'a', 'b')
('a', 'a', 'c')
('a', 'b', 'b')
('a', 'b', 'c')
('a', 'c', 'c')
('b', 'b', 'b')
('b', 'b', 'c')
('b', 'c', 'c')
('c', 'c', 'c')
"""

for p in combinations_with_replacement(items, 2):
    print(p)

"""
output
('a', 'a')
('a', 'b')
('a', 'c')
('b', 'b')
('b', 'c')
('c', 'c')
"""
