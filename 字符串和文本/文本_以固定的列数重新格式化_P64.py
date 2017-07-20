"""
textwrap()模块
"""
import textwrap
import os

s = 'I want to eat, I want to eat, I want to eat, \
I want to eat, I want to eat, I want to eat \
I want to eat.'

# 指定每行的长度,initial_indent指定第一行的开头字符， subsequent_indent指定剩余行的开头字符
print(textwrap.fill(s, 30, initial_indent='111', subsequent_indent='222'))
"""
输出
111I want to eat, I want to
222eat, I want to eat, I want
222to eat, I want to eat, I
222want to eat I want to eat.
"""
