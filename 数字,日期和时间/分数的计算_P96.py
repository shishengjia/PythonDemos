"""
fractions模块
"""
from fractions import Fraction

a = Fraction(1, 2)
b = Fraction(3, 4)
print(a + b) # 5/4

c = a + b
print(c.numerator) # 5 分子
print(c.denominator) # 4 分母

print(float(c)) # 1.25 转化为小数
print(c.limit_denominator(8))

x = 0.625
print(Fraction(*x.as_integer_ratio())) # 5/8 小数化分数
