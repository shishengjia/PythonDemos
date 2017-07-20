"""
enumerate()函数
"""

# 例子一，给错误信息行加上行号

def parse_data(filename):
    with open(filename, "rt") as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
        try:
            count = int(fields[1])
            ...
        except ValueError as e:
            # 错误信息添加行号
            print("Line {}: Parse error: {}".format(lineno, e))

例子二,打印每个单词出现过的行号

from collections import defaultdict

# 所出现过的行号用列表来存储
word_summary = defaultdict(list)

with open("../test2.txt", "r") as f:
    for idx, line in enumerate(f, 1):
        # 将句子分解成单词
        words = [w.strip().lower() for w in line.split()]
        # 记录每个单词所在行号
        for word in words:
            word_summary[word].append(idx)
    for key, value in word_summary.items():
        print("{} : {}".format(key, value))


"""
output
want : [1]
in : [3]
eating : [2, 3]
interested : [3]
am : [3]
eat : [1]
like : [2]
to : [1]
i : [1, 2, 3]
"""


"""
当在元组序列上应用该函数时，不能将元组本身展开
"""
data = [(1, 2), (3, 4), (5, 6)]

# correct
for idx, (x, y) in enumerate(data, 1)

# error
for idx, x, y in enumerate(data, 1)
