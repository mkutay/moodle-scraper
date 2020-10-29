import urllib.parse
import urllib.request
import http.cookiejar
import login # Yazdigimiz kodu importluyoruz
import findCourses
import isHomework
import ssl
import os
import sendMail
import json
import sys
import getTime

args = sys.argv

if os.path.isdir(".files/") == False:
    os.system("mkdir .files")

if os.path.isfile(".moodle_bot_info.txt") == False or (len(args) > 1 and args[1] == '--login'):
    username = input('Kullanici adin nedir? ')
    password = input('Sifren nedir? ')
    recever_mail = input('Mailin nedir? ')
    info = {'username': username, 'password': password, 'recever_mail': recever_mail}
    with open('.moodle_bot_info.txt', 'w') as outfile:
        json.dump(info, outfile)

info = {}

with open('.moodle_bot_info.txt') as json_file:
    info = json.load(json_file)

if login.scraper_login(info['username'], info['password']) == -1: # Yazdigimiz kodu cagriyoruz giris yapmasi icin
    exit()

tmp = findCourses.findCourses() # Ders ismini ve linkini aliyor
names = tmp[0]
links = tmp[1]

if len(names) == 0 or len(links) == 0:
    print("Odevin yok!! Ya da bir hata var.")
    exit()

homeworks = []

for i in range(len(names)):
    messages = isHomework.isHomework(links[i], names[i]) # Her ders icin odev var mi diye kontrol ediyor

    for j in range(len(messages)):
        remaining_time = ""
        if 'assign' in messages[j][2]:
            remaining_time = getTime.remTime(messages[j][2], messages[j][1])
        else:
            remaining_time = "Sure yok"
        homeworks.append(messages[j][0] + " odevin var! Odevin adi: " + messages[j][1] + ". Odevin icin kalan sure: " + remaining_time + ". Odevin linki: " + messages[j][2] + ".")

main_message = ""

for i in range(len(homeworks)):
    main_message += homeworks[i]
    main_message += '\n';

print(main_message)

sendMail.send_mail("Odevlerin var!", main_message, info['recever_mail'])
