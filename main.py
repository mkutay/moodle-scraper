import urllib.parse
import urllib.request
import http.cookiejar
import login # Yazdigimiz kodu importluyoruz
import findCourses
import isHomework
import ssl
import os

if os.path.isdir(".files/") == False:
    os.system("mkdir .files")

login.scraper_login() # Yazdigimiz kodu cagriyoruz giris yapmasi icin

ssl._create_default_https_context = ssl._create_unverified_context # Sertifika sorununu cozen sihirli satir

tmp = findCourses.findCourses()
names = tmp[0]
links = tmp[1]

for i in range(len(names)):
    isHomework.isHomework(links[i], names[i])
