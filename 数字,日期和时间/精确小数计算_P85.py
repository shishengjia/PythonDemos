
"""
浮点数计算会有误差
"""
a = 4.2
b = 2.1
print(a + b) # 6.300000000000001
print((a + b) == 6.3) #False

"""
期望更高的精度可以使用decimal模块
"""
from decimal import Decimal

a = Decimal('4.2')
b = Decimal('2.1')
print(a+b) # 6.3
print((a + b) == Decimal('6.3'))  # True

"""
对数字的位数进行控制，需要创建一个本地的上下文环境然后修改其设定
"""
from decimal import localcontext

a = Decimal('3.2')
b = Decimal('1.7')

with localcontext() as ctx:
    ctx.prec = 3
    print(a / b) # 1.88

with localcontext() as ctx:
    ctx.prec = 20
    print(a / b) # 1.8823529411764705882


"""
float提供17位的精度，如果对精度没有很高的要求，一般使用普通的浮点类型，性能上相比decimal也快上很多
"""

"""
另外，大数和小数加在一起的时候需小心
"""
print(sum([1.23e+18, 1, -1.23e+18])) # 0.0

import math

print(math.fsum([1.23e+18, 1, -1.23e+18])) # 1.0
