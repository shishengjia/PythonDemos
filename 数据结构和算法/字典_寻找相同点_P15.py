
"""
字典的keys()方法返回keys-view对象，支持常见的集合操作
字典的items()方法返回(key,value)对象，也支持常见的集合操作
但字典的values()对象不支持集合操作。但是必须执行操作的话，可以先将值转化为集合来实现
"""
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# keys in common
a.keys() & b.keys()

# keys in a that are not in b
a.keys() - b.keys()

# find (key, value)pairs in common
a.items() & b.items()

# 去除字典中的某些键
c = {key:a[key] for key in a.keys() - {'z'}}
print(c)
