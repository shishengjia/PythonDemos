"""
只有一个分隔符时，可以直接使用str.split()方法
"""

s = 're root txt fast'
print(s.split()) # 默认是空格

"""
针对多个分隔符，使用re模块下的split()方法
"""
import re

# 详细的正则表达式用法可以参考Python核心编程第一章
s2 = 'HearthStone   ;War\jkjj:123'
print(re.split(r'[\s\\;:]+', s2)) # ['HearthStone', 'War', 'jkjj', '123']

# 如果使用捕获组的话，匹配的文本也会在最终结果中
fields = re.split(r'(\s|\\|;|:)+', s2)
print(fields) # ['HearthStone', ';', 'War', '\\', 'jkjj', ':', '123']

values = fields[::2]
delimiters = fields[1::2] + ['']
print(values) # 得到分解后的字符串
print(delimiters) # 得到分隔符
