# coding: utf-8
import csv
import numpy


filename = 'ch02-data.csv'

data = []
reader = None
header = None

try:
    with open(filename) as f:
        reader = csv.reader(f)
        header = next(reader)
        data = [row for row in reader]

except csv.Error as e:
    print('Error reading CSV file at line %s: %s' % (reader.line_num, e))

if header:
    print(header)
    print('===============')

for data_row in data:
    print(data_row)
