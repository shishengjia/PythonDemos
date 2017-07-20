"""
代码中如果有很多硬编码的索引值，可读性会很差.
"""

record = '20 15.5'
COUNT = slice(0, 2)
PRICE = slice(3, 7)
total_cost = int(record[COUNT]) * float(record[PRICE])
print(total_cost)
