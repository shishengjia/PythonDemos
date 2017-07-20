"""
可以使用内建的reversed()函数实现反向迭代
条件是对象拥有确定的大小，或者实现了__reversed__()方法
"""

a = [1, 2, 3, 4]
for x in reversed(a):
    print(x, end=' ') # 4 3 2 1


"""
如果条件无法满足，必须先将对象转换为列表 reversed(list(item))
但这种方式比较消耗内存
所以可以通过实现__reversed__()，这样就无需先把数据放到列表中
"""

class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        """
        自定义迭代模式
        """
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n < self.start:
            yield n
            n += 1

for i in CountDown(5):
    print(i, end=' ') # 4 3 2 1

for i in reversed(CountDown(5)):
    print(i, end=' ') # 1 2 3 4
