"""
对单独的数值做格式化输出，使用format()即可
"""

x = 1234.56789
print(format(x, '0.2f')) # 1234.57
print(format(x, '>10.1f')) #    1234.6
# 千位分隔符
print(format(x, ',')) # 1,234.56789
# 千位分隔符&保留一位小数
print(format(x, '0,.1f')) # 1,234.6
# 科学计数法
print(format(x, 'e')) # 1.234568e+03
print(format(x, '0.2e')) # 1.23e+03
