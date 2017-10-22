# encoding: utf-8
"""
@author: shishengjia
@time: 2017/10/12 下午12:45
"""
"""
this format can be read in almost the same way as CSV fles, 
as the Python module csv supports so-called dialects that 
enable us to use the same principles to read variations of 
similar fle formats—one of them being the tab delimited format.
"""
import csv


file_name = 'ch02-data.tab'

# data = []
# reader = None
# header = None
#
# try:
#     with open(file_name) as f:
#         reader = csv.reader(f, dialect=csv.excel_tab)
#         header = next(reader)
#         data = [row for row in reader]
# except csv.Error as e:
#     print(e)
#
# if header:
#     print(header)
#     print('===========')
#
# for item in data:
#     print(item)

file_name_2 = 'ch02-data-dirty.tab'

data = []
reader = None
header = None

try:
    with open(file_name) as f:
        reader = csv.reader(f, dialect=csv.excel_tab)
        header = next(reader)
        # 去除制表符
        data = [row[0].strip().split('\t') for row in reader]
except csv.Error as e:
    print(e)

if header:
    print(header)
    print('===========')

for item in data:
    print(item)