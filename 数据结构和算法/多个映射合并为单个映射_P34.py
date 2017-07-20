"""
ChainMap()函数
它维护的是原始字典，原始字典的值改变了，它的值也降改变
"""
from collections import ChainMap

a = [1, 2, 3]
b = [3, 4, 5]
c = ChainMap(a, b)
for x in c:
    print(x, end=' ')
# 输出 1 2 3 4 5 重复的值过滤

a = {
    'x': 1,
    'y': 2
}

b = {
    'x': 3,
    'y': 2
}

c = ChainMap(a, b)
print(c['x']) # 1 如果有重复的键，采用第一个映射中所对应的值

"""
使用dict自己的update()方法，但要注意，为了不破坏原始数据，需要构建一个完整的字典对象
而且其中任何一个原始字典中的值改变了，这个改动不会反应到合并后的字典中去
"""
d = a
d.update(b)
print(d)
