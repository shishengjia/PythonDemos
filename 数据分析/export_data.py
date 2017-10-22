# encoding: utf-8
import os
import sys
import argparse
from io import StringIO, BytesIO
import struct
import json
import csv
import xlwt
from numpy import genfromtxt
"""
@author: shishengjia
@time: 2017/10/12 下午1:29
"""


def import_data(import_file):
    """
    excepts to find fixed width row
    Sample row: 161322597 0386544351896 0042
    """

    mask = '9s14s5s'
    data = []
    count = 0
    with open(import_file, 'rb') as f:
        for line in f:
            count += 1
            # unpack line to tuple
            fields = struct.Struct(mask).unpack_from(line)
            # strip any whitespace for each field
            # pack everything in a list and add to full dataset
            data.append(list([f.strip() for f in fields]))

            if count == 1000:
                break
    return data


def write_data(data, export_format):
    """
    Dispatches call to a specific transformer and returns data set.
    Exception is xlsx where we have to save data in a file
    """
    if export_format == 'csv':
        return write_csv(data)
    elif export_format == 'json':
        return write_json(data)
    elif export_format == 'xlsx':
        return write_xlsx(data)
    else:
        raise Exception('Illegal format defined')


def write_csv(data):
    """
    transformes data into csv
    returns csv as string
    """
    f = StringIO()
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

    # get the content of the file-like object
    return f.getvalue()


def write_json(data):
    """
    transformes data into json
    """
    j = json.dumps(data)
    return j


def write_xlsx(data):
    """
    writes data into xlsx file
    """
    book = xlwt.Workbook()
    sheet_1 = book.add_sheet('Sheet 1')
    row = 0
    for line in data:
        col = 0
        for data in line:
            sheet_1.write(row, col, str(data, 'utf-8'))
            col += 1

        row += 1

        if row > 100:
            break

    # XLS is special case, we have to save the file and just return 0
    f = StringIO()
    f.seek(0)
    # todo something wrong with this
    book.save(f)
    return f.getvalue()


data = import_data('ch02-fixed-width-1M.data')
print(write_data(data, 'xlsx'))
