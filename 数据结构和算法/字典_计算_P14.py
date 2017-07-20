
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20
}

# 为了比较股票价格，可以利用zip()将字典的键和值反转过来
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

# 对数据进行排序
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

"""
需要注意的是zip()创建了一个迭代器，它的内容只能被消费一次
"""
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names)) # ok
print(max(prices_and_names)) # ValueError,不能进行第二次使用

"""
另外需要注意的是当涉及(values, key)对的比较时，如果有多个条目value相同，
那么将用key作为判断依据
"""
