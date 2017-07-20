"""
字节串已经支持大多数和文本字符串一样的内建操作
字节串相对字符串效率高，但是推荐使用字符串
"""
data = b'Hello World'
print(data[:5]) # b'Hello'
print(data.startswith(b'Hello')) # True
print(data.split()) # [b'Hello', b'World']

"""
在字节串上执行正则表达式的模式匹配操作，但是模式本身需要以字节串的形式来指定
"""
import re

data = b'FOO:BAR,SPAM'
print(re.split(b'[:,]', data)) # [b'FOO', b'BAR', b'SPAM']

"""
和字符串的区别：
    输出方面的区别
    字节串没有像普通字符串那样的格式化操作
"""
a = 'Hello world'
print(a[0]) # H
print(a) # Hello world

b = b'Hello world'
print(b[0]) # 72
print(b) # b'Hello world'
# 想要像字符串那样打印出来,得先解码
print(b.decode('ascii')) # Hello world
