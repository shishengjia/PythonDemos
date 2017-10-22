# coding: utf-8
from pprint import pprint
import xlrd

file = 'ch02-xlsxdata.xlsx'

wb = xlrd.open_workbook(filename=file)

# all_sheets = wb.sheets()
# print(all_sheets)

ws = wb.sheet_by_name('Sheet1')

data_set = []

for r in range(ws.nrows):  # 行
    col = []
    for c in range(ws.ncols):  # 列
        col.append(ws.cell(r, c).value)
    data_set.append(col)

pprint(data_set)
