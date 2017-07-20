# -*- coding: utf-8 -*-
from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode("ascii")

datafile = StringIO(data)
csvReader = csv.reader(datafile)
for row in csvReader:
    print(row)



"""
DictReader会把csv文件的每一行转换成python的字典对象，而不是列表对象
除了第一行的字段列表保存在变量dictReader.fieldnames里
"""
dictReader = csv.DictReader(datafile)

print(dictReader.fieldnames)

for row in dictReader:
    print(row)
