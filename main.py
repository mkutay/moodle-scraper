#!/usr/bin/env python3
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
from lxml import html
session_requests = requests.session()

# sitemiz
# baska bir site yazinca calisiyor ama moodle'da calismiyor
login_url = 'https://arionline.ariokullari.k12.tr/login/index.php'
result = session_requests.get(login_url)

tree = html.fromstring(result.text)
# giris yaparken kullanacagimiz login token'i aliyoruz
authenticity_token = list(set(tree.xpath("//input[@name='logintoken']/@value")))[0]

# kullanici adi, sifre, logintoken'i
payload = {
    "username": "",
    "password": "",
    "logintoken": authenticity_token
}

# giris yapmaya calisiyoruz
result = session_requests.post(
    login_url,
    data = payload,
    headers = dict(referer=login_url)
)

# asil bilgileri alacagimiz yer
url = 'https://arionline.ariokullari.k12.tr/course/view.php?id=232'
result = session_requests.get(
    url,
    headers = dict(referer = url)
)

# yeni odev var mi diye bakiyor.
tree = html.fromstring(result.content)
bucket_names = tree.xpath("//div[@class='activityinstance']/a/text()")

# varsa yazdiriyor
print(bucket_names)
