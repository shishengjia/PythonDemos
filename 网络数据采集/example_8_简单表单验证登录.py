import requests

params = {
    'username': 'Tyan',
    'password': 'password'
}

"""
自己管理cookies
"""
r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print("Cookies is set to dict:")
print(r.cookies.get_dict())
print("--------------------")
print("Going to profile page")
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)
print(r.text)

"""
session自动管理cookies等信息
"""
session = requests.Session()

s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print("Cookies is set to dict:")
print(s.cookies.get_dict())
print("--------------------")
print("Going to profile page")
s = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(r.text)
