"""
字典推导式
"""
prices = {
    'PythonCookBook': 87,
    'Django': 56,
    'Flask': 34,
    'CorePython': 85
}

# 大于80元的书
d1 = {key:value for key, value in prices.items() if value > 80}
print(d1)

"""
创建元组序列然后传给dict()
显然字典推导式更加清晰，而且运行效率更高
"""
d2 = dict((key,value) for key, value in prices.items() if value > 80)
print(d2)
