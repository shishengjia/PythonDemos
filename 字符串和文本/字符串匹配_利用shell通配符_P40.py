"""
使用fnmatch模块下的fnmatch()和fnmatchcase()
前者采用的大小写区分规则和底层文件系统相同，后者则完全根据我们提供的大小写方式来匹配
"""

from fnmatch import fnmatch, fnmatchcase


print(fnmatch('foo.txt', '*.txt')) # True
print(fnmatch('foo.txt', '?oo.txt')) # True
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

"""
处理非文件名式的字符串时的用处
"""
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W CRANV AVE',
    '2122 N CLARK ST',
    '4802 N BROASA'
]

list_1 = [address for address in addresses if fnmatchcase(address, '* ST')]
print(list_1) # ['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']
