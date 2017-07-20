from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError

try:
    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
except HTTPError as e:
    print(e)

try:
    bsObj = BeautifulSoup(html)
    # 找到所有标签为span， class属性为green的元素
    names = bsObj.findAll("span", {"class": "green"})
except AttributeError as e:
    print(e)

for name in names:
    # 通过get_text()函数提取标签里的内容
    print(name.get_text())
