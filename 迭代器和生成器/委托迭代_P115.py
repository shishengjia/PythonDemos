"""
自定义一个容器对象，使其完成迭代操作
一般是定义__iter__()方法
Python的迭代协议要求__iter__返回一个特殊的迭代器对象，由该对象实现的__next__方法
来完成实际的迭代
"""

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)

for ch in root:
    print(ch)

"""
output
Node(1)
Node(2)
"""
