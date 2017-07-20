"""
strip() 去除左右两端
lstrip() 去除左端
rstrip() 去除右端
都不能去除中间的字符
"""
s = '---hello---hello---'
print(s.strip('-')) # hello---hello
print(s.lstrip('-')) # hello---hello---
print(s.rstrip('-')) # ---hello---hello

"""
去除中间的字符，使用replace()或正则表达式
"""
print(s.replace('-', '')) # hellohello

import re
print(re.sub('-+', '', s)) # hellohello
