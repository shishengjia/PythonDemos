# -*- coding: utf-8 -*-
"""
希望只通过关键字的形式接受特定的参数
通过将关键字参数放置在*打头的参数或者是一个单独的*之后
"""


def recv(maxsize, *, block):
    pass

recv(1024, block=True)
# recv(1024, True)  # TypeError: recv() takes 1 positional argument but 2 were given
