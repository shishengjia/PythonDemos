"""
通过complex(real,ima)
"""
a = complex(2, 4)
print(a.conjugate()) # (2+4j) 共轭值
print(a.real) # 2.0 实部
print(a.imag) # 4.0 虚部
"""
或者浮点数加后缀j来实现
"""
print(3 - 5j) # (3-5j)

"""
常见的算术运算操作都适用于复数
Python中的标准数学函数不会产生复数值，要产生复数结果必须明确使用cmath
"""
import math
import cmath

# print(math.sqrt(-1)) # error
print(cmath.sqrt(-1)) # 1j
