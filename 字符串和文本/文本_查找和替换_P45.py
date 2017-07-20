"""
对于简单的文本模式，使用str.replace()即可
"""
text = 'apple find the apple'
print(text.replace('apple', 'pear')) # pear find the pear

"""
对于更复杂的模式，可以使用re模块中的sub()方法
"""
import re

text = 'Today is 11/27/2012. PyCon starts 3/12/2013'

# 先将模式进行编译，在执行重复替换时有更好的性能
datepat = re.compile(r'(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)')

print(datepat.sub(r'\g<year>-\g<month>-\g<day>', text)) # Today is 2012-11-27. PyCon starts 2013-3-12

"""
对于更加复杂的情况，需要指定一个替换回调函数
"""
from calendar import month_abbr

def change_date(m):
    # 用group()方法提取匹配中特定的部分
    month_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), month_name, m.group(3))

print(datepat.sub(change_date, text)) # Today is 27 Nov 2012. PyCon starts 12 Mar 2013


