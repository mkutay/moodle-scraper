import requests

cookies = {
    'MoodleSession': 'olejbrro3hr5jqva949dj9noo5',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="86", "\\"Not\\\\A;Brand";v="99", "Google Chrome";v="86"',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://arionline.ariokullari.k12.tr',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://arionline.ariokullari.k12.tr/mod/assign/view.php?id=5788&action=editsubmission',
    'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
}

data = {
  'lastmodified': '1603555650',
  'id': '5788',
  'userid': '429',
  'action': 'savesubmission',
  'sesskey': 'n2qKBiw90o',
  '_qf__mod_assign_submission_form': '1',
  'files_filemanager': '326857940',
  'submitbutton': 'De\u011Fi\u015Fiklikleri kaydet'
}

response = requests.post('https://arionline.ariokullari.k12.tr/mod/assign/view.php', headers=headers, cookies=cookies, data=data)

