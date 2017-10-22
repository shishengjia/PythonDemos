# encoding: utf-8
"""
@author: shishengjia
@time: 2017/10/12 下午12:25
"""
import struct
import string


data_file = 'ch02-fixed-width-1M.data'

# define how to understand line of data from the file
# this means that a string of width 9 characters
# followed by a string width of 15 characters
# further followed by a string of 5 characters
mask = '9s14s5s'

with open(data_file, 'rb') as f:
    for line in f:
        fields = struct.Struct(mask).unpack_from(line)
        print('fields: ', [field.strip() for field in fields])