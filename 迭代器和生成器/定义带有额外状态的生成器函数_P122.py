"""
通过类来实现，将生成器函数定义在__iter__()方法中
这样就可以将额外状态作为类的属性和方法提供给用户交互
"""

from collections import deque

class LineHistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            # 记录搜查历史
            self.history.append((lineno, line))
            yield line

    def clear(self):
        """
        清空记录
        """
        self.history.clear()

    def print_history(self):
        """
        打印历史记录
        """
        for lineno, line in self.history:
            print('{}:{}'.format(lineno, line))

with open('../test.txt') as f:
    lines = LineHistory(f)
    for line in lines:
        # 如果捕捉到Python，则输出该行并显示最近3次的历史记录
        if 'Python' in line:
            print("Got Python!!!    ", line)
            lines.print_history()
            print('-' * 30)

"""
output
Got Python!!!     Python is powerful

3:>>>>>>>>>>>>>>>>>>>>>>>>>

4:Man:The question is

5:Python is powerful

------------------------------
Got Python!!!     I like Python

4:Man:The question is

5:Python is powerful

6:I like Python

------------------------------
"""
