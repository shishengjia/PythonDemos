"""
使用str.startswith(),str.endswith()
需要注意的是在传入参数时不能传入列表或者集合，必须首先转化成tuple
"""

filename = 'spam.txt'
print(filename.endswith('.txt')) # True

url = 'http://www.python.org'
print(url.startswith('http:')) # True

import os

filenames = os.listdir('../') # 上一层目录下的文件
print(filenames)
# 查找py文件
pyfile = [name for name in filenames if name.endswith('.py')]
print(pyfile)
