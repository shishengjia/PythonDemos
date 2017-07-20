"""
针对 text = "foo = 23 + 42 * 10"做分词处理
"""

# 第一步定义所有可能的标记，包括空格,通过正则表达式中的命名捕获组来实现
import re

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

# 第二步使用模式对象的scanner()方法完成分词操作

from collections import namedtuple

# 引入命名元组存储信息
Token = namedtuple('Token', ['type', 'value'])

def generate_tokens(pat, text):
    # 创建一个扫描对象
    scanner = pat.scanner(text)
    # 重复调用match()一次匹配一个模式
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

tokens = (tokens for tokens in generate_tokens(master_pat, 'foo = 23 + 42 * 10') if tokens.type != 'WS')

for token in tokens:
    print(token)

"""
output
Token(type='NAME', value='foo')
Token(type='EQ', value='=')
Token(type='NUM', value='23')
Token(type='PLUS', value='+')
Token(type='NUM', value='42')
Token(type='TIMES', value='*')
Token(type='NUM', value='10')
"""

"""
注意点:
    1.对于每个可能出现的文本序列，都要确保有对应的模式来识别，如果有任何不能匹配的文本，扫描将停止
    2.上面的标记在正则表达式中的顺序同样重要，如果某个模式是另一个较长模式的子串，就必须确保较长的那个模式先做匹配
"""

LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'

master_pat = re.compile('|'.join([LE, LT, EQ]))
# 这样会把文本'<='匹配为'<'紧跟着'=',而没有匹配为单独的标记'<='
# master_pat = re.compile('|'.join([LT, LE, EQ])) # 错误
