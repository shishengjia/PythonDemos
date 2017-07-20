"""
使用collections中的Counter类，其输入必须是可哈希的对象。
在底层实现中，Counter是一个字典，在元素和他们出现的次数间做了映射
"""

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes',
    'it\'s', 'my', 'eyes',
]
word_counts = Counter(words)
# 次数前3的单词
top_three = word_counts.most_common(3)
print(top_three)

morewords = ['into', 'more', 'eyes']
# 更新统计
word_counts.update(morewords)
new_top_three = word_counts.most_common(3)
print(new_top_three)

"""
Counter对象结合数学运算操作使用
"""
a = Counter(words)
b = Counter(morewords)
# 加号跟采用update方法的结果相同
print(a + b)
# 减号则跟加号相反
print(a - b)
