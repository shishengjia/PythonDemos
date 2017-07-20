# -*- coding: utf-8 -*-
"""
该代码适用于windows环境
由于windows的cmd，默认codepage是CP936，即GBK的编码，所以需要先将得到的Unicode先编码为GBK，然后再在cmd中显示出来，
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import re
import string

def cleanInput(input, n):
    """
    排列成n个连续单词组成的序列
    """
    # 清洗数据
    input = re.sub("\n+", " ", input)
    input = re.sub(" +", " ", input)
    input = re.sub("\[[0-9]*\]", "", input)
    # 内容转换成utf-8格式以消除转义字符
    input = input.encode("utf-8")
    input = input.decode("ascii", "ignore")
    cleaned_inputt = []
    input = input.split(" ")
    for item in input:
        # 清理单词两边的任何标点符号
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleaned_inputt.append(item)
    return cleaned_inputt

def getNgrams(input, n):
    input = cleanInput(input, 2)
    output = dict()
    for i in range(len(input)-n+1):
        newNGram = " ".join(input[i:i+n])
        if newNGram in output:
            output[newNGram] += 1
        else:
            output[newNGram] = 1
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
ngrams = getNgrams(content, 2)
# 针对频率进行排序，使用OrderedDict存储
ngrams = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))
print(ngrams)
