from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for item in items:
        # 如果是可迭代对象，则将这个对象作为子例程进行递归，但是忽略str和bytes类型
        if isinstance(item, Iterable) and not isinstance(item, ignore_types):
            yield from flatten(item)
        else:
            yield item

for x in flatten([1, 2, ['abc', 'xy', [3, 4, 5]], 6, 7]):
    print(x)

"""
output
1
2
abc
xy
3
4
5
6
7
"""
