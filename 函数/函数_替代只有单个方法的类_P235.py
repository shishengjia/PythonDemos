# -*- coding: utf-8 -*-
from urllib.request import urlopen


class URLTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        print(kwargs)  # {'names': 'IBM,AAPL,FB', 'fields': 'sllclv'}
        return urlopen(self.template.format_map(kwargs))


yahoo = URLTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo.open(names='IBM,AAPL,FB', fields='sllclv'):
    print(line.decode('utf-8'))

print('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}'.
      format_map({'names': 'IBM,AAPL,FB', 'fields': 'sllclv'}))

# http://finance.yahoo.com/d/quotes.csv?s=IBM,AAPL,FB&f=sllclv

"""
使用只有单个方法的类的原因是保存额外的状态给类方法使用
但是使用嵌套函数或者说闭包会更加优雅
闭包的核心特性是它可以记住定义闭包时的环境，比如下面的例子中opener函数可以记住参数template的值
"""


def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener

yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo(names='IBM,AAPL,FB', fields='sllclv'):
    print(line.decode('utf-8'))