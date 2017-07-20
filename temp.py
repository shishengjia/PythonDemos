import re

text = "经验5-10年 "
text_ = text.strip('/').strip()
pat = re.compile('.*?(\d+).+?(\d+).*')
match_obj = pat.match(text_)
print(match_obj.group(2))
