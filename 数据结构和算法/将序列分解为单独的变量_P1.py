# 只要对象可迭代，就能执行分解操作
a, b, c = [1, 2, 3]
print(a, b, c)

a, b, c = (1, 2, 3)
print(a, b, c)

a, b, c = '123'
print(a, b, c)
