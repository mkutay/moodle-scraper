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
import getHomeworks
import check
import htmlOut

args = sys.argv

if os.path.isdir(".files/") == False:
    os.system("mkdir .files")

if os.path.isfile(".moodle_bot_info.json") == False or '--login' in args:
    username = input('Kullanici adin nedir? ')
    password = input('Sifren nedir? ')
    recever_mail = input('Mailin nedir? ')
    sender_mail = input("Botun maili ne? ")
    sender_pass = input("Botun sifresi ne? ")
    info = {'username': username, 'password': password, 'recever_mail': recever_mail, 'sender_mail': sender_mail, 'sender_pass': sender_pass}
    with open('.moodle_bot_info.json', 'w') as outfile:
        json.dump(info, outfile)

info = {}

with open('.moodle_bot_info.json') as json_file:
    info = json.load(json_file)

if login.scraper_login(info['username'], info['password']) == -1: # Yazdigimiz kodu cagriyoruz giris yapmasi icin
    exit()

homeworks = getHomeworks.sendHomework(info, args)

# print(homeworks)

if '--sendAll' in args:
    main_message = ""
    main_message2 = []
    for i in range(len(homeworks)):
        main_message2.append(homeworks[i]["className"] + " dersinde odevin var. " + "Odevin adi " + homeworks[i]["homeworkName"] + ". Odevin icin Kalan sure " + homeworks[i]["remTime"] + ". Odevin linki " + homeworks[i]["url"] + ".")
        main_message += homeworks[i]["className"] + " dersinde odevin var. " + "Odevin adi " + homeworks[i]["homeworkName"] + ". Odevin icin Kalan sure " + homeworks[i]["remTime"] + ". Odevin linki " + homeworks[i]["url"] + "."
        main_message += "\n"
    htmlOut.out(main_message2, homeworks)
    sendMail.send_mail("Odevlerin var!",
                       main_message,
                       info['recever_mail'],
                       info['sender_mail'],
                       info['sender_pass'])

if '--check' in args:
    check.check(homeworks, info)

# if '--timerCheck' in args:
