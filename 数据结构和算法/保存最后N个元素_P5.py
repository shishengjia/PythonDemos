from collections import deque

"""
对指定文本做简单的匹配
使用collection.deque，当有新纪录插入，且队列已满，会自动移除最老的那条记录
从队列两端插入或者移除元素，复杂度仅为O(1),而列表为O(N)
"""
def search(lines, pattern, history_size=5):
    previous_lines = deque(maxlen=history_size)
    for line in lines:
        # 当发现有匹配时就输出当前的匹配行以及最后检查过的N行文本
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

with open("../test.txt") as f:
    for line, prevlines in search(f, 'Python', 3):
        print(list(prevlines))
        print(line, end='')
        print('-'*20)
