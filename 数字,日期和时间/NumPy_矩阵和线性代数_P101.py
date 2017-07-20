"""
使用NumPy中的matrix对象
"""

import numpy as np

m = np.matrix([
    [1, -2, 3],
    [0, 4, 5],
    [7, 8, -9]
])

# 矩阵转置
print(m.T)
"""
output
[[ 1  0  7]
 [-2  4  8]
 [ 3  5 -9]]
"""

# 创建一个向量并与矩阵相乘
v = np.matrix([
    [2],
    [3],
    [4]
])
print(m * v)
"""
output
[[ 8]
 [32]
 [ 2]]
"""
