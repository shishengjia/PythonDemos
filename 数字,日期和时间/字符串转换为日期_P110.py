# from datetime import datetime as dt
#
# # 字符串转换datetime对象
# text = '2012-09-20'
# y = dt.strptime(text, '%Y-%m-%d')
# print(y) # 2012-09-20 00:00:00
#
# # datetime对象转化为字符串
# nice_y = dt.strftime(y, '%A %B %d, %Y')
# print(nice_y) # Thursday September 20, 2012
#
# """
# 需要注意的是strptime()是用纯Python代码写的，性能比较差，如果在代码中解析大量的日期，且事先知道日期的格式，
# 那么自己实现一个解决方案会更有效率
# """
#
# def pares_ymd(s):
#     year, month, day = s.split('/')
#     return dt(int(year), int(month), int(day))
#
# m = pares_ymd('2017/11/12')
# print(m) # 2017-11-12 00:00:00
print('\u9a8c\u8bc1\u7801\u9519\u8bef')
