"""
如果一个对象是可哈希的，那么在它的生存周期内必须是不可变的，它需要有一个__hash__()方法
整数，浮点数，字符串，元组都是不可变的
"""

# 序列中的值是可哈希的，可以通过使用集合和生成器
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 2, 2, 3, 4, 5]
print(list(dedupe(a)))
