"""
random模块
"""
import random

"""
修改初始的种子值的几种方法
"""
random.seed()
random.seed(12345)
random.seed(b'bytedata')

values = [1, 33, 22, 11, 10]

# 从序列中随机挑选元素
print(random.choice(values)) # 33

# 取样出N个元素
print(random.sample(values, 3)) # [1, 10, 11]

# 原地打乱(不是新产生一个序列)序列中元素的顺序

values2 = [3, 45, 32, 11]
random.shuffle(values2)
print(values2)

# 随机产生一个范围内的整数

print(random.randint(10, 20))

# 产生0-1之间均匀分布的浮点数值
print(random.random())

# N个随机比特位表示的整数

print(random.getrandbits(10))
