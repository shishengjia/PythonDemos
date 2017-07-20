"""
需要注意的是NumPy的array中的元素必须都是同一类型，否则会被强制转换
"""

import numpy as np

# python list
x = [1, 2, 3]
y = [4, 5, 6]
print(x * 2) # [1, 2, 3, 1, 2, 3]
print(x + y) # [1, 2, 3, 4, 5, 6]
# print(x + 10) # error

# NumPy arrays
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print(ax * 2) # [2 4 6 8]
print(ax + 10) # [11 12 13 14]
print(ax + ay) # [ 6  8 10 12]
print(ax * ay) # [ 5 12 21 32]

# NumPy提供一些函数
print(np.sqrt(ax)) # [ 1.          1.41421356  1.73205081  2.        ]
print(np.sin(ax)) # [ 0.84147098  0.90929743  0.14112001 -0.7568025 ]

# NumPy扩展了Python列表的索引功能
a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

# 第'1'行的所有元素
print(a[1]) # [5 6 7 8]

# 第'0'列的所有元素
print(a[:, 0]) # [1 5]

# 选取第‘1’列到第‘2’列的元素
print(a[:, 1:3])
# [[2 3]
#  [6 7]]

# 筛选大于3的元素
print(a[a > 3]) # [4 5 6 7 8]
