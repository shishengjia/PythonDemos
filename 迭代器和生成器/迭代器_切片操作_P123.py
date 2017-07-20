"""
由于不知道迭代器和生成器的长度，所以无法执行普通的切片操作
使用itertools.islice()函数
"""
import itertools

def count(n):
    x = 1
    while x <= n:
        yield x
        x += 1

cd = count(10)

for x in itertools.islice(cd, 5, 7):
    print(x, end=' ') # 6 7

"""
需要注意的是islice()产生的是一个迭代器，但是它丢弃了索引之前的元素
索引之后的元素还会继续输出
"""

for x in cd:
    print(x, end=' ') # 8 9 10
