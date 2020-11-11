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
import sendHomeworkMail

args = sys.argv

if os.path.isdir(".files/") == False:
    os.system("mkdir .files")

if os.path.isfile(".moodle_bot_info.json") == False or (len(args) > 1 and args[1] == '--login'):
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

if '--sendAll' in args:
    sendHomeworkMail.sendHomework(info)
