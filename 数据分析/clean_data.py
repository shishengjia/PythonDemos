# -*- coding: utf-8 -*-
"""
Python数据处理127页
"""
from csv import DictReader, reader
from datetime import datetime
import numpy as np
import pprint
print np.array([[1, 2, 3]]) + [2, 2, 2]

# data_rdr = DictReader(open('mn.csv', 'rb'))
# header_rdr = DictReader(open('mn_headers.csv', 'rb'))
#
# data_rows = [d for d in data_rdr]
# header_rows = [h for h in header_rdr]

# pprint.pprint(data_rows[:5])
# pprint.pprint(header_rows[:5])

# 数据清洗1
# new_rows = []
# for data_dict in data_rows:  # 遍历每一行数据
#     new_row = {}
#     for dkey, dval in data_dict.items():  # 遍历每一对键值对
#         for header_dict in header_rows:  # 遍历每一行标题数据
#             if dkey in header_dict.values():  # 如果该对键值对的键存在于该行标题数据所有键值对的值中
#                 new_row[header_dict.get('Label')] = dval
#     new_rows.append(new_row)
#
# pprint.pprint(new_rows[0])

# 数据清洗2
data_rdr = reader(open('mn.csv', 'rb'))
header_rdr = reader(open('mn_headers_updated.csv', 'rb'))

data_rows = [r for r in data_rdr]
header_rows = [h for h in header_rdr if h[0] in data_rows[0]]  # 筛选匹配的标题

print(len(header_rows))

all_short_headers = [h[0] for h in header_rows]

skip_index = []
# 由于数据集中的标题行与标题文件中的标题的顺序不一致，因此重新整理标题行
first_header_rows = []

for header in data_rows[0]:
    if header not in all_short_headers:  # 标题不再标题集中，就记录该标题索引
        index = data_rows[0].index(header)
        skip_index.append(index)
    else:
        for head in header_rows:
            if head[0] == header:
                first_header_rows.append(head)
                break

new_data = []

for row in data_rows[1:]:
    new_row = []
    for i, d in enumerate(row):
        if i not in skip_index:
            new_row.append(d)
    new_data.append(new_row)

zipped_data = []
for drow in new_data:
    zipped_data.append(zip(first_header_rows, drow))

# pprint.pprint(zipped_data)
# 检查标题是否匹配
# data_headers = []
# for i, header in enumerate(data_rows[0]):
#     if i not in skip_index:
#         data_headers.append(header)
# header_match = zip(data_headers, first_header_rows)
# pprint.pprint(header_match)

# 数据格式化
example_dict = {
    'float_number': 1324.321325493,
    'very_large_integer': 43890923148390284,
    'percentage': .324,
}

string_to_print = 'float: {float_number:.4f}\n'
string_to_print += 'interger: {very_large_integer:,}\n'
string_to_print += 'percentage: {percentage:.2%}'
print string_to_print.format(**example_dict)

# for i, data in enumerate(zipped_data[0][:20]):
#     print i, data

# 日期格式化1(采访开始时间)
start_time_string = "{}/{}/{} {}:{}".format(zipped_data[0][8][1], zipped_data[0][7][1], zipped_data[0][9][1],
                                            zipped_data[0][13][1], zipped_data[0][14][1])
start_time = datetime.strptime(start_time_string, '%m/%d/%Y %H:%M')
print start_time

# 日期格式化2(采访结束时间)
end_time = datetime(int(zipped_data[0][9][1]), int(zipped_data[0][8][1]), int(zipped_data[0][7][1]),
                    int(zipped_data[0][15][1]), int(zipped_data[0][16][1]))
print end_time

duration = end_time - start_time
print duration.total_seconds() / 60.0, duration.days

# 日期对象转字符串
print end_time.strftime('%m/%d/%Y %H:%M:%S')
print start_time.ctime()
print start_time.strftime('%Y-%m-%dT%H:%M:%S')