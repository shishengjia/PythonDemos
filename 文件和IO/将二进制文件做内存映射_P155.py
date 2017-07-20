# -*- coding: utf-8 -*-
"""
使用mmap模块实现对文件的内存映射操作,对数据的任何修改都会拷贝回原来的文件中
如果只想本地修改数据，并不想将这些修改写回到原始文件，使用mmap.ACCESS_COPY
"""

import os
import mmap

def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


# 创建一个初始文件
size = 10000
with open('data.bin', 'wb') as f:
    f.seek(size-1)
    f.write(b'\x00')

# mmap()返回的mmap对象也可以当做上下文管理器使用，底层的文件会自动关闭
with memory_map('data.bin') as m:
    print(len(m)) # 10000
    print(m[0]) # 0
    m[0:11] = b'Hello World'

with memory_map('data.bin') as m:
    print(m[0:10]) # b'Hello Worl'
