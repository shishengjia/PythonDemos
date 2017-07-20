"""
使用itemgetter
sorted()函数接受一个关键字参数key，该参数代表一个可调用对象
itemgetter()接受的参数作为查询的标记，从rows中提取需要的值
类似sorted()的函数如min(),max()也支持这种操作
"""
from operator import itemgetter

rows = [
    {'fname': 'Jack', 'uid': 1003},
    {'fname': 'Tom', 'uid': 1001},
    {'fname': 'Marry', 'uid': 1002},
    {'fname': 'Bone', 'uid': 1005},
    {'fname': 'Anna', 'uid': 1004}
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

# itemgetter()函数还可以接受多个键
rows_by_id_name = sorted(rows, key=itemgetter('uid', 'fname'))

"""
有时会用lambda表达式取代itemgetter()的功能，rows_by_fname = sorted(rows, key=lambda r:r['fname'])
但是用itemgetter()运行更快
"""
