from bs4 import BeautifulSoup as bs

import requests

cookies = {
    'MoodleSession': '3aggkvevm9b94h4ju163ch9b56',
}

login_url = "https://arionline.ariokullari.k12.tr/"

s = requests.session()
logintoken = s.get(login_url, verify=False).cookies['logintoken']

print(logintoken)

data = {
  'username': '',
  'password': '',
  'anchor': '',
  'logintoken': logintoken
}

response = requests.post('https://arionline.ariokullari.k12.tr/login/index.php', cookies=cookies, data=data)
print(login_req.status_code)
