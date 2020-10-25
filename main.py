import urllib.parse
import urllib.request
import http.cookiejar
import login # Yazdigimiz kodu importluyoruz
import findCourses
import isHomework
import ssl
import os
import sendMail

if os.path.isdir(".files/") == False:
    os.system("mkdir .files")

login.scraper_login() # Yazdigimiz kodu cagriyoruz giris yapmasi icin

ssl._create_default_https_context = ssl._create_unverified_context # Sertifika sorununu cozen sihirli satir

tmp = findCourses.findCourses() # Ders ismini ve linkini aliyor
names = tmp[0]
links = tmp[1]

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

if len(names) == 0 or len(links) == 0:
    print("Odevin yok!! Ya da bir hata var.")
    exit()

main_message = ""

for i in range(len(names)):
    messages = isHomework.isHomework(links[i], names[i]) # Her ders icin odev var mi diye kontrol ediyor

    message = ""

    for i in range(len(messages)):
        message += str(messages[i])
        message += "\n"

    if len(message) == 0:
        continue

    main_message += message

sendMail.send_mail("Odevlerin var!", main_message)
