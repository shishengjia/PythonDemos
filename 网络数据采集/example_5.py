# -*- coding: utf-8 -*-
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import os

dowloadedpath = os.path.abspath(os.path.dirname(__file__) + "\images4")
print(dowloadedpath)
if not os.path.exists(dowloadedpath):
    os.makedirs(dowloadedpath)

html = urlopen("http://www.mmjpg.com/mm/952")
bs_obj = BeautifulSoup(html)

images = set()
# 提取img的src值
image_pat = re.compile('.*(srcs|src)="(.*?)".*')
for image in bs_obj.find("div", {"class": "content"}).findAll("img"):
    images.add(image_pat.match(str(image)).group(2))

count = 1
url = "http://img.mmjpg.com/2017/898/{}.jpg"
for i in range(45):
    # print(image)
    count += 1
    urlretrieve(url.format(count), dowloadedpath + "\\" + str(count) + ".jpg")
