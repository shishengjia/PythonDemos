# -*- coding: utf-8 -*-
"""
原型设计模式（Prototype design pattern）帮助我们创建对象的克隆，其最简单的形式就是一
个clone()函数，接受一个对象作为输入参数，返回输入对象的一个副本。在Python中，这可以
使用copy.deepcopy()函数来完成。

copy.deepcopy() 深复制
深副本构造一个新的复合对象后，会递归地将在原始对象中找到的对象的副本插入新对
象中。

copy.copy() 浅复制
浅副本构造一个新的复合对象后，（会尽可能地）将在原始对象中找到的对象的引用插入
新对象中。关注提升应用性能和优化内存使用
"""
import copy
from collections import OrderedDict


class A:
    def __init__(self):
        self.x = 18
        self.message = 'Hello'


class B(A):
    def __init__(self):
        A.__init__(self)
        self.y = 36

    def __str__(self):
        return '{} {} {}'.format(self.x, self.message, self.y)


# if __name__ == '__main__':
#     b = B()
#     c = copy.deepcopy(b)
#     print([str(i) for i in (b, c)])  # ['18 Hello 36', '18 Hello 36']
#     print([i for i in (b, c)])  # [<__main__.B object at 0x01B55AF0>, <__main__.B object at 0x01BFC290>]

"""
使用原型模式创建一个展示图书信息的应用
"""


class Book:
    def __init__(self, name, authors, price, **rest):
        self.name = name
        self.authors = authors
        self.price = price
        print(self.__dict__)
        # 将rest 的内容添加到Book类的内部字典中，成为它的一部分
        self.__dict__.update(rest)
        print(self.__dict__)

    def __str__(self):
        my_list = []
        # 使用有序字典进行存储, 确保每次输出一致
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            my_list.append('{} : {}'.format(i, ordered[i]))
            if i == 'price':
                my_list.append('$')
            my_list.append('\n')
        return ''.join(my_list)


class Prototype:
    """
    register()和unregister()，这两个方法用于在一个字典中追踪被克隆的对象。注意这仅是一个方便之举，并没有实质性的作用.
    """
    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError('Incorrect object identifier: {}'.format(identifier))
        obj = copy.deepcopy(found)
        # 更新已经改变的值
        obj.__dict__.update(attr)
        return obj


def main():
    b1 = Book('The C Programming Language', ('Brian W. Kernighan', 'Dennis M.Ritchie'), price=118,
              publisher='Prentice Hall', length=228, publication_date='1978-02-22',
              tags=('C', 'programming', 'algorithms', 'data structures'))
    prototype = Prototype()
    cid = 'k&r-first'
    prototype.register(cid, b1)
    b2 = prototype.clone(cid, name='The C Programming Language(ANSI)', price=48.99, length=274,
                         publication_date='1988-04-01', edition=2)
    for i in (b1, b2):
        print(i)
        print("ID b1 : {} != ID b2 : {}".format(id(b1), id(b2)))

main()