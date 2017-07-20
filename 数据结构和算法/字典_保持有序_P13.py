# 使用OrderedDict
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
for key, value in d.items():
    print(key, ':', value)

# 想在JSON编码时精确控制各字段顺序，只需要现在OrderedDict中构建数据就可以了
import json

print(json.dumps(d))

"""
OrderedDict内部维护了一个双向列表，它的大小是普通字典的2倍多，使用时需谨慎
"""
