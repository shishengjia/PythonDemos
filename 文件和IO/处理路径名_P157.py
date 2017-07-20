# -*- coding: utf-8 -*-
"""
os.path模块
"""
import os

# 当前路径
print(__file__) # F:\PythonDemo\PythonCookBook\文件和IO\处理路径名_P157.py

# 所在目录路径
print(os.path.dirname(__file__)) # F:\PythonDemo\PythonCookBook\文件和IO

# 当前文件
print(os.path.basename(__file__)) # 处理路径名_P157.py

# 组合路径
print(os.path.join('D:\\Users', 'Picture', os.path.basename(__file__))) # D:\Users\Picture\处理路径名_P157.py

# 获取绝对路径
print(os.path.abspath('F:/PythonDemo/PythonCookBook/文件和IO')) # F:\PythonDemo\PythonCookBook\文件和IO

# 扩展至用户目录
print(os.path.expanduser('~/处理路径名_P157.py')) # C:\Users\shishengjia/处理路径名_P157.py

# 分离扩展名
print(os.path.splitext(__file__)) # ('F:\\PythonDemo\\PythonCookBook\\文件和IO\\处理路径名_P157', '.py')
