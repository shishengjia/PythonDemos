

rows = [
    {'address': 'N3 511', 'date': '07/01/2012'},
    {'address': 'N4 411', 'date': '07/04/2012'},
    {'address': 'N3 240', 'date': '07/02/2012'},
    {'address': 'N6 111', 'date': '07/03/2012'},
    {'address': 'N7 234', 'date': '07/02/2012'},
    {'address': 'N1 432', 'date': '07/02/2012'},
]

from operator import itemgetter
from itertools import groupby

# 首先要根据感兴趣的字段对数据进行排序
# 因为groupby()只能检查连续项
rows.sort(key=itemgetter('date'))

for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for item in items:
        print(item)
"""
07/01/2012
{'address': 'N3 511', 'date': '07/01/2012'}
07/02/2012
{'address': 'N3 240', 'date': '07/02/2012'}
{'address': 'N7 234', 'date': '07/02/2012'}
{'address': 'N1 432', 'date': '07/02/2012'}
07/03/2012
{'address': 'N6 111', 'date': '07/03/2012'}
07/04/2012
{'address': 'N4 411', 'date': '07/04/2012'}
"""

"""
如果只是根据日期将数据分组到一起，放进一个大的数据结构中心以允许进行随机访问，那利用
defaultdict()构建一个一键多值字典会更好。
注意的是，不考虑内存的话，这种方式相对上面一种方式要更快
"""

from collections import defaultdict

rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
