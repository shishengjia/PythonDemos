from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

def get_title(url):
    try:
        # 打开url链接
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        # 读取网页内容
        bsObj = BeautifulSoup(html, "html.parser")
        print(bsObj)
        # 提取标题
        title = bsObj.h1
    except AttributeError as e:
        return None

    return title

title = get_title("http://www.pythonscraping.com/pages/page1.html")
if title:
    print(title)
else:
    print("Title could not be found!")
