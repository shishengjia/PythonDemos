# 希望保留元素插入的顺序，使用列表
d = {
    'a': [1, 2, 3],
    'b': [4, 5, 6]
}

# 希望消除重复元素且不在意它们的顺序，使用集合
e = {
    'a': {1, 2, 3},
    'b': {4, 5, 6}
}

# 使用defaultdict， 它会自动初始化第一个值,这样就不必写繁琐的初始化代码d[key] = []
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)
d['b'].append(4)
print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(3)
d['b'].add(4)
print(d)
