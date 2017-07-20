"""
使用ljust()，rjust(),center()
"""

text = 'hello'
# 默认是空格，这里使用*进行填充
print(text.ljust(10, '*')) # hello*****
print(text.rjust(10, '*')) # *****hello
print(text.center(10, '*')) # **hello***

"""
使用format()
< 左对齐
> 右对齐
^ 中间对齐
"""
print(format(text, '<10'))
print(format(text, '>10'))
print(format(text, '^10'))

# 指定填充字符
print(format(text, '*<10'))
print(format(text, '*>10'))
print(format(text, '*^10'))

# 格式化多个值
print('{:*>10} {:*>10}'.format('hello', 'world')) # *****hello *****world

"""
format()能作用于任何值，不仅限于字符
"""
x = 1.234
print(format(x, '*>10')) # *****1.234
