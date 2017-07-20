import re

str_pat = re.compile(r'\"(.*)\"')
text_1 = 'Computer says "no"'
print(str_pat.findall(text_1)) # ['no']

text_2 = 'Computer says "no" phone says "yes"'
print(str_pat.findall(text_2)) # ['no" phone says "yes']

"""
从上面可以看出，模式r'\"(.*)\"'匹配包含在引号中的文本，但是*操作符采用贪心策略，匹配
过程是基于找出最长的可能匹配来进行的，所以text_2的匹配时错误的
在*后加上?修饰符即可
"""
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text_2)) # ['no', 'yes']
