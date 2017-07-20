"""
通过float()来创建无穷大，负无穷大和NaN
"""
import math

a = float('inf')
b = float('-inf')
c = float('nan')

# 检测
print(math.isinf(a)) # True
print(math.isinf(b)) # True
print(math.isnan(c)) # True

"""
关于这些特殊的浮点数值的可能问题请参见书本
"""
