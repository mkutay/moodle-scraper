import requests

cookies = {
    'MoodleSession': 'olejbrro3hr5jqva949dj9noo5',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Chromium";v="86", "\\"Not\\\\A;Brand";v="99", "Google Chrome";v="86"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryutxvYAyTCo2KHIt9',
    'Accept': '*/*',
    'Origin': 'https://arionline.ariokullari.k12.tr',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://arionline.ariokullari.k12.tr/mod/assign/view.php?id=5788&action=editsubmission',
    'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
}

params = (
    ('action', 'upload'),
)

data = '$------WebKitFormBoundaryutxvYAyTCo2KHIt9\\r\\nContent-Disposition: form-data; name="repo_upload_file"; filename="mat eis 8. foy.pdf"\\r\\nContent-Type: application/pdf\\r\\n\\r\\n\\r\\n------WebKitFormBoundaryutxvYAyTCo2KHIt9\\r\\nContent-Disposition: form-data; name="sesskey"\\r\\n\\r\\nn2qKBiw90o\\r\\n------WebKitFormBoundaryutxvYAyTCo2KHIt9\\r\\nContent-Disposition: form-data; name="repo_id"\\r\\n\\r\\n4\\r\\n------WebKitFormBoundaryutxvYAyTCo2KHIt9\\r\\nContent-Disposition: form-data; name="itemid"\\r\\n\\r\\n326857940\\r\\n------WebKitFormBoundaryutxvYAyTCo2KHIt9\\r\\nContent-Disposition: form-data; name="author"\\r\\n\\r\\nMEHMET KUTAY BOZKURT\\r\\n------WebKitFormBoundaryutxvYAyTCo2KHIt9\\r\\nContent-Disposition: form-data; name="savepath"\\r\\n\\r\\n/\\r\\n------WebKitFormBoundaryutxvYAyTCo2KHIt9\\r\\nContent-Disposition: form-data; name="title"\\r\\n\\r\\nmat eis 8. foy.pdf\\r\\n------WebKitFormBoundaryutxvYAyTCo2KHIt9\\r\\nContent-Disposition: form-data; name="ctx_id"\\r\\n\\r\\n12430\\r\\n------WebKitFormBoundaryutxvYAyTCo2KHIt9--\\r\\n'

response = requests.post('https://arionline.ariokullari.k12.tr/repository/repository_ajax.php', headers=headers, params=params, cookies=cookies, data=data)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://arionline.ariokullari.k12.tr/repository/repository_ajax.php?action=upload', headers=headers, cookies=cookies, data=data)

