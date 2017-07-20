from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

def get_bsObj(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html)
    except AssertionError as e:
        return None

    return bsObj
