# encoding: utf-8
from pprint import pprint
import requests
"""
@author: shishengjia
@time: 2017/10/12 下午1:07
"""

# this url expired
url = 'https://github.com/timeline.json'

r = requests.get(url)
json_obj = r.json()

repos = set()

print(json_obj)

for entry in json_obj:
    try:
        repos.add(entry['documentation_url'])
    except KeyError as e:
        print('No key %s. Skipping...' % e)

pprint(repos)
