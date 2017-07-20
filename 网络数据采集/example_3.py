from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)

# 打印table下所有子标签
for child in bsObj.find("table", {"id": "giftList"}).children:
    print(child)

# 打印table下除了表格标题外的所有子标签
# tr获得第一个子标签，及表格标题所在标签，next_siblings获得后面的所有子标签
for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)

# image的父标签td的上一个标签的内容
print(bsObj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

# 注意这里调用了两次next_sibling函数，因为两个标签之间其实还有其他元素，比如换行符
print(bsObj.find("table", {"id": "giftList"}).tr.next_sibling.next_sibling)

# 利用正则表达式查找所有商品的图片的url链接
for img in bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts\/img\d+\.jpg")}):
    print(img["src"])
