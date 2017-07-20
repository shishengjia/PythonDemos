# -*- coding: utf-8 -*-

"""
将数据读取到预分配好的数组中，使用文件对象的readinto()方法，中间不经过拷贝环节,且可以在
原地修改数据
"""
import os


def read_into_buffer(filename):
    # 开辟一块空间
    buf = bytearray(os.path.getsize(filename))
    # 将二进制文件写到buf中
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf

with open('sample.bin', 'wb') as f:
    f.write(b'Hello World')

buf = read_into_buffer('sample.bin')
print(buf) # bytearray(b'Hello World')

# 原地修改数据
buf[:5] = b'HELLO'
print(buf) # (b'HELLO World')

"""
使用内存映像memoryview可以使我们对已存在的缓冲区做切片处理，中间不涉及任何拷贝动作
"""
m1 = memoryview(buf)
m2 = m1[-5:]
m2[:] = b'WORLD'
print(buf) # bytearray(b'HELLO WORLD')
