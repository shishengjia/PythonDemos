# -*- coding: utf-8 -*-
import os

# 获取目录下的所有文件，子目录(不包括子目录下的文件)，符号链接
print(os.listdir('../'))

# 获取目录下的子目录
dirs = [name for name in os.listdir('../') if os.path.isdir(os.path.join('../', name))]
print(dirs)

# 获取目录下的文件
files = [name for name in os.listdir('../') if os.path.isfile(os.path.join('../', name))]
print(files)

# 获取目录下的所有py文件
py_files = [name for name in os.listdir('../') if name.endswith('.py')]
print(py_files)

# 文件名的匹配
import glob
print(glob.glob('../*.py'))

from fnmatch import fnmatch

print([name for name in os.listdir('../') if fnmatch(name, '*.py')])

# 获取文件名，以及文件大小和修订日期
# 直接获取对应信息
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name)) for name in pyfiles]

# 使用meta = os.stat(filename) meta.st_size meta.st_mtime ...
filemetadata = [(name, os.stat(name)) for name in pyfiles]
