import requests

cookies = {
    'MoodleSession': 'olejbrro3hr5jqva949dj9noo5',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Chromium";v="86", "\\"Not\\\\A;Brand";v="99", "Google Chrome";v="86"',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Origin': 'https://arionline.ariokullari.k12.tr',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://arionline.ariokullari.k12.tr/mod/assign/view.php?id=5788&action=editsubmission',
    'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
}

params = (
    ('action', 'list'),
)

data = {
  'sesskey': 'n2qKBiw90o',
  'client_id': '5f951a3d8a542',
  'filepath': '/',
  'itemid': '326857940'
}

response = requests.post('https://arionline.ariokullari.k12.tr/repository/draftfiles_ajax.php', headers=headers, params=params, cookies=cookies, data=data)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://arionline.ariokullari.k12.tr/repository/draftfiles_ajax.php?action=list', headers=headers, cookies=cookies, data=data)

