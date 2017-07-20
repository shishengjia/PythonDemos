# -*- coding: utf-8 -*-
import csv
import json
import xlrd
import pprint
import slate
from xml.etree import ElementTree as ET
from pdftables import get_tables

# with open('D:/Downloads/data-text.csv', 'rb') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print row

# with open('D:/Downloads/data-text.csv', 'rb') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print row

# with open('data-text.json') as f:
#     json_data = f.read()
#     data = json.loads(json_data)
#     for item in data:
#         print item


# tree = ET.parse('data-text.xml')
# root = tree.getroot()
# data = root.find('Data')
# all_data = []
#
# for observation in data:
#     record = {}
#     for item in observation:
#         lookup_key = item.attrib.keys()[0]
#         if lookup_key == 'Numeric':
#             rec_key = 'NUMERIC'
#             rec_value = item.attrib['Numeric']
#         else:
#             rec_key = item.attrib[lookup_key]
#             rec_value = item.attrib['Code']
#         record[rec_key] = rec_value
#     all_data.append(record)
# print all_data

# book = xlrd.open_workbook('SOWC 2014 Stat Tables_Table 9.xlsx')
# sheet = book.sheet_by_name('Table 9 ')
#
# count = 0
# data = {}
# for i in range(14, 210):
#     row = sheet.row_values(i)
#     country = row[1]
#     data[country] = {
#         'child_labor': {
#             'total': [row[4], row[5]],
#             'male': [row[6], row[7]],
#             'female': [row[8], row[9]],
#         },
#         'child_marriage':{
#             'married_by_15': [row[10], row[11]],
#             'married_by_18': [row[12], row[13]],
#         }
#     }
# print data['Afghanistan']
# pprint.pprint(data)


def clean(line):
    """
    清洗代码中的换行符、空格以及其他特殊符号
    """
    line = line.strip('\n').strip()
    line = line.replace('\xe2\x80\x93', '-')
    line = line.replace('\xe2\x80\x99', '\'')

    return line


def turn_on_off(line, status, start, prev_line, end='\n'):
    """
    这个函数用于检查该行是否以特定值开始/结束。
    如果该行确实以特定值开始/结束，则状态设为开/关（真/假）。
    """
    if line.startswith(start):
        status = True
    elif status:
        if line == end and prev_line != 'and areas':
            status = False
    return status

countries = []
totals = []
previous_line = ''
double_lined_countries = [
    'Bolivia (Plurinational \n',
    'Democratic People\xe2\x80\x99s \n',
    'Democratic Republic \n',
    'Lao People\xe2\x80\x99s Democratic \n',
    'Micronesia (Federated \n',
    'Saint Vincent and \n',
    'The former Yugoslav \n',
    'United Republic \n',
    'Venezuela (Bolivarian \n',
]
# 该行是否是国家名
# country_line = total_line = False
# with open('en-final-table9.txt', 'r') as f:
#     for i, line in enumerate(f, 1):
#         if country_line:
#             if previous_line in double_lined_countries:
#                 line = ' '.join([clean(previous_line), clean(line)])
#                 countries.append(line)
#             elif line not in double_lined_countries:
#                 countries.append(clean(line))
#         if total_line:
#             if len(line.replace('\n', '').strip()) > 0:
#                 totals.append(clean(line))
#
#         country_line = turn_on_off(line, country_line, 'and areas', previous_line)
#         total_line = turn_on_off(line, total_line, 'total', previous_line)
#         previous_line = line
#
# data = dict(zip(countries, totals))
# pprint.pprint(data)

# headers = [
#     'Country', 'Child Labor 2005-2012 (%) total',
#     'Child Labor 2005-2012 (%) male',
#     'Child Labor 2005-2012 (%) female',
#     'Child Marriage 2005-2012 (%) married by 15',
#     'Child Marriage 2005-2012 (%) married by 18',
#     'Birth registration 2005-2012 (%)',
#     'Female Genital mutilation 2002-2012 (prevalence), women',
#     'Female Genital mutilation 2002-2012 (prevalence), girls',
#     'Female Genital mutilation 2002-2012 (support)',
#     'Justification of wife beating 2005-2012 (%) male',
#     'Justification of wife beating 2005-2012 (%) female',
#     'Violent discipline 2005-2012 (%) total',
#     'Violent discipline 2005-2012 (%) male',
#     'Violent discipline 2005-2012 (%) female'
# ]
#
# with open('EN-FINAL_Table_9.pdf', 'rb') as f:
#     all_tables = get_tables(f)
#
# for table in all_tables:
#     for row in table[5:]:
#         if row[2] == '':
#             print row

