import requests

headers = {
    'sec-ch-ua': '"Chromium";v="86", "\\"Not\\\\A;Brand";v="99", "Google Chrome";v="86"',
    'Referer': 'https://arionline.ariokullari.k12.tr/mod/assign/view.php?id=5788&action=editsubmission',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
}

response = requests.get('https://arionline.ariokullari.k12.tr/theme/image.php/lambda/core/1599906147/i/menu', headers=headers)

