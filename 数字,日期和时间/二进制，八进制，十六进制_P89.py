"""
将整数转化为相应进制的字符串形式
"""

x = 1234

print(bin(x)) # 0b10011010010
print(oct(x)) # 0o2322
print(hex(x)) # 0x4d2

"""
消除0b,0o,0x前缀
"""
print(format(x, 'b')) # 10011010010
print(format(x, 'o')) # 2322
print(format(x, 'x')) # 4d2

"""
字符串形式的整数转换为不同的进制
"""
print(int('4d2', 16)) # 1234
print(int('10011010010', 2)) # 1234
