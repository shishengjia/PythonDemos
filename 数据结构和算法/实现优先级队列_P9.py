import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    """
    连续使用heappop()方法将依次从小到大返回元素
    针对此特性，将priority值取反，那么priority值越大，将越先被返回
    另外，在优先值相等的情况下，将通过_index进行比较，先进来的元素_index小，那么将先被返回
    注意不使用_index的话,元素的优先值相等的话将导致程序崩溃
    """
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue();
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

for i in range(4):
    print(q.pop())
"""
(-5, 1, Item('bar'))
(-4, 2, Item('spam'))
(-1, 0, Item('foo'))
(-1, 3, Item('grok'))
"""
