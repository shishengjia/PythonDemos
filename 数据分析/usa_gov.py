# coding=utf-8
# 对时区进行计数
from collections import defaultdict, Counter
from pandas import DataFrame, Series
import numpy
import pandas
import matplotlib.pyplot as plt
import json
with open('usa_gov.txt') as f:
    datas = [json.loads(line) for line in f.readlines() if 'tz' in line]

# 提取时区字段timezone
records = [data['tz'] for data in datas if 'tz' in data]


# Python实现
def get_counts_1(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts

top = [(count, tz) for tz, count in get_counts_1(records).items()]
top.sort()
# print top[-10:]

# 或者直接使用Counter类
# print(Counter(records).most_common(10))

# 下面是用pandas实现
frame = DataFrame(datas)
print(frame['tz'].value_counts()[:10])

clean_tz = frame['tz'].fillna('Missing')  # 替换缺失值
clean_tz[clean_tz == ''] = 'Unknown'  # 替换未知值
tz_counts = clean_tz.value_counts()
tz_counts[:10].plot(kind='barh', rot=0)
plt.show()  # 显示图表