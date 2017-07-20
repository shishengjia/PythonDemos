# -*- coding: utf-8 -*-
from tempfile import TemporaryFile

"""
由TemporaryFile创建的文件都是未命名的，在目录中也没有对应的条目
"""
with TemporaryFile('w+t') as f:
    f.write("Hello world")
    # 文件指针指向头，并读取内容
    f.seek(0)
    print(f.read())


from tempfile import NamedTemporaryFile

"""
指定delete参数为False，文件在关闭时将不会自动删除
"""
with TemporaryFile('w+t', delete=False) as f:
    print(f.name)
    f.write("Hello world")
    # 文件指针指向头，并读取内容
    f.seek(0)
    print(f.read())
