# -*- coding: utf-8 -*-
"""
使用pickle将Python对象序列化，方便传输和存储
"""

import pickle

# 对象序列化
data = [1, 2, 3]
with open('pickle_example', 'wb') as f:
    pickle.dump(data, f)

with open('pickle_example', 'rb') as f:
    print(pickle.load(f)) # [1, 2, 3]

# 对象转储为字符串
s = pickle.dumps(data)
print(s) # b'\x80\x03]q\x00(K\x01K\x02K\x03e.'
print(pickle.loads(s)) # [1, 2, 3]
