"""
datetime模块
"""
from datetime import timedelta

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b

# 天数
print(c.days) # 2

# 小时(不把天算进去)
print(c.seconds / 3600) # 10.5

# 总共多少小时
print(c.total_seconds() / 3600) # 58.5


from datetime import datetime as dt

a = dt(2012, 9, 23)

# 日期加10天
print(a + timedelta(days=10)) # 2012-10-03 00:00:00

b = dt(2012, 11, 16)
# a和b之间相差的天数
print((b-a).days) # 54

# 当前时间
print(dt.today())

"""
需要处理更复杂的日期时间处理问题，可以安装python-dateutil包

"""
