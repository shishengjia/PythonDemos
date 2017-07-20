"""
对各种操作加上re.IGNORECASE标记
"""
import re

text = 'UPPER PYTHON, lower python, Mixed Python'

print(re.findall('python', text, flags=re.IGNORECASE)) # ['PYTHON', 'python', 'Python']

pattern = re.compile('python')
# 但是有局限，待替换的文本与匹配的文本大小写不吻合
print(re.sub('python', 'snake', text, flags=re.IGNORECASE)) # UPPER snake, lower snake, Mixed snake

"""
写一个支撑函数解决上面问题
"""

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)) # UPPER SNAKE, lower snake, Mixed Snake
