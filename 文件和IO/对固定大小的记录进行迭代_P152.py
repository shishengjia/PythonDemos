# -*- coding: utf-8 -*-
"""
使用iter()和functools.partial()函数
"""
from functools import partial

# 每次都4个字节的数据
RECORD_SIZE = 4

with open('sample.bin', 'rb') as f:
    # b''的作用是哨兵值，当读取到文件结尾时就会返回这个值，迭代结束
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r)
"""
output
b'Hell'
b'o Wo'
b'rld'
"""
