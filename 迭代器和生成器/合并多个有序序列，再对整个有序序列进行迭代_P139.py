"""
heapq.merge()函数要求所有的输入序列是有序的
"""
import heapq

a = [1, 2, 3, 4]
b = [5, 6, 7]

for x in heapq.merge(a, b):
    print(x)

"""
合并两个有序的文件
"""
with open('../file1.text', 'rt') as f1, open('../file2.text', 'rt') as f2, \
    open('../file3.text', 'wt') as w:
    for line in heapq.merge(f1, f2):
        w.write(line)
