

s1 = 'Spicy Jalape\u00f1'
s2 = 'Spicy Jalapen\u0303'

print(s1, s2) # Spicy Jalapeñ Spicy Jalapen~
print(s1==s2) # False

"""
上述例子中的s1和s2是同一个文本，但是是两种不同的表示形式，s1采用的是全组成形式，而
s2采用的是组合形式.
所以应先将文本统一为规范形式，通过unicodedata模块
"""

import unicodedata

# 指定字符串的规范表示-NFC全组成
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1, t2) # Spicy Jalapeñ Spicy Jalapeñ
print(t1==t2) # True

# 指定字符串的规范表示-NFD组合字符
t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3, t4) # Spicy Jalapen~ Spicy Jalapen~
print(t3==t4) # True

"""
从文本中去除音符标记
当然只有组合型字符能去音标，所以先用combining()函数判断字符是否为一个组合型字符
"""
print(''.join(c for c in t3 if not unicodedata.combining(c))) # Spicy Jalapen
