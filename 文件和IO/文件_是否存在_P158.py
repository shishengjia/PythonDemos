# -*- coding: utf-8 -*-
import os

# 文件是否存在
print(os.path.exists('data.bin'))

# 是否是文件
print(os.path.isfile('data.bin')) # True

# 是否是目录
print(os.path.isdir('data.bin')) # False

# 是否是符号链接文件
os.path.islink

# 文件大小
print(os.path.getsize('data.bin'))

# 获取文件创建时间
import time
print(time.ctime(os.path.getctime('data.bin'))) # Thu Apr 20 10:36:01 2017
