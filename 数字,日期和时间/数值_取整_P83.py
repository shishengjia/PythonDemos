"""
对一个浮点数取整到固定的小数位，使用内建的round(value, ndigits)函数
"""
print(round(1.23, 1)) # 1.2
print(round(1.27, 1)) # 1.3
print(round(1.5, 0)) # 2.0
print(round(2.5, 0)) # 2.0

# ndigits为负数的时候，会相应地取整到十位，百位等
print(round(12488, -1)) # 12490
print(round(12488, -2)) # 12500

"""
如果只是将数值以固定的位数输出，一般不用round函数，只要在格式化时指定进度进行
"""
x = 1.23456
print(format(x, '0.2f')) # 1.23
print('{:0.3f}'.format(x)) #1.235
