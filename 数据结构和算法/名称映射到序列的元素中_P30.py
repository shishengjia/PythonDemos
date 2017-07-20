"""
使用namedtuple()
"""
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age'])
p = Person('Jack', 22)
print(p)

# namedtuple支持所有普通元组所支持的操作
print(len(p))

# 索引
print(p[0])

# 分解
name, age = p
print(name, age)

"""
namedtupled的一种可能用法是作为字典的替代，更节约空间。
如果要构建涉及字典的大型数据结构，namedtupled会更高效
但是需要注意namedtupled是不可变的，需要修改属性的话可以使用namedtuple实例的_replace()，该方法创建一个全新的命名元组
"""
p = p._replace(age=23)
print(p)

"""
_replace可以作为一种简便的方法填充具有可选或缺失字段的命名元组
"""
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# 创建一个包含默认值的"原型"元组
stock_prototype = Stock('', 0, 0.0, None, None)

# 创建一个方法，使用_replace返回一个新的实例

def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price':123.21}
a_ = dict_to_stock(a)
print(a_)

"""
最后，需要注意的是，如果目标是定义一个高效的数据结构，而且将来会修改各种实例属性，那么
可以考虑定义一个使用_slots_属性的类
"""
