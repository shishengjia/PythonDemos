"""
合并在一个序列或可迭代对象中的字符串,使用字符串的join()方法
只是想链接两个单独的字符串，用 + 即可
"""

parts = ['I', 'want', 'to', 'eat']
print(' '.join(parts)) # I want to eat
print(','.join(parts)) # I,want,to,eat

"""
需要注意的是+操作符每次都会创建一个新的字符串对象，效率低下，比较好的做法是先收集所有
要连接的部分，然后用join()方法一次性连接
"""

# 利用生成器表达式
data = ['ACME', 50, 90.1]
print(','.join(str(d) for d in data)) # ACME,50,90.1

# 在打印的时候，比较三种操作
a, b, c = 'I', 'want', 'to'
print(a + ' ' + b + ' ' + c) # 不推荐
print(' '.join([a, b, c])) # 不推荐
print(a, b, c, sep=' ') # 推荐
