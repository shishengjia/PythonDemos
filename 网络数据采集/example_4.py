from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote
from urllib.error import HTTPError
import json
import re

"""
由于百度的反爬机制，只能获取历史版本的第一页数据
"""


def getCountry(ipAddress):
    response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("country_code")


def seach_history(item_name):
    """
    搜索百度词条的历史编辑者
    """
    # 基础url
    base_url = "https://baike.baidu.com"
    # url末尾添加搜索词
    item_url = base_url + "/item/" + item_name
    # 打开网页
    item_html = urlopen(item_url)
    # BeautifulSoup进行处理
    bs_obj_item = BeautifulSoup(item_html)
    # 找到历史记录url
    history_url = base_url + bs_obj_item.find("dd", {"class": "description"}).find("a")["href"]
    get_all_history(history_url, 2)


def get_all_history(url, count=1):
    history_users = set()
    try:
        # 打开历史记录页面
        html = urlopen(url + "#page" + str(count))
    except HTTPError as e:
        return None
    bs_obj = BeautifulSoup(html)
    # 找到编辑者标签并提取名字
    for user in bs_obj.findAll("a", {"class": "uname"}):
        user_text = user.get_text()
        history_users.add(user_text)
    # 打印
    for user in history_users:
        print(user)



seach_history(quote("what"))
