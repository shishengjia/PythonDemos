"""
使用正则表达式和re模块
"""
import re

text1 = '11/27/2012'
text2 = '11-27-2012'


datepat = re.compile(r'\d+/\d+/\d+')
print(datepat.match(text1).group()) # 11/27/2012
print(datepat.match(text2)) # None

# match()方法总是尝试在字符串的开头找到匹配，所以下面的text3是无法匹配的
text3 = '/11/27/2012'
print(datepat.match(text3)) # None

# 使用findall()方法,搜索出文本中所有的匹配项
print(datepat.findall(text3)) # ['11/27/2012']

"""
使用捕获组，简化后续对文本的处理
"""
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m.group(0)) # 11/27/2012
print(m.group(1)) # 11
print(m.group(2)) # 27
print(m.group(3)) # 2012
print(m.groups()) # ('11', '27', '2012')

m = datepat.findall(text3)
print(m) # [('11', '27', '2012')]

"""
想以迭代的方式找出匹配项，可以使用finditer()方法
"""

"""
注意一下，match()只会检查字符串的开头，要想精确匹配，需要加一个结束标记$
对比下面两组的输出结果
"""
datepat2 = re.compile(r'(\d+)/(\d+)/(\d+)$')
print(datepat2.match('11/27/2012asddsa')) # None
print(datepat2.match('11/27/2012')) # find

datepat3 = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat3.match('11/27/2012asddsa')) # find
print(datepat3.match('11/27/2012'))  # find
