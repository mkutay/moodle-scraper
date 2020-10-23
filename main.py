import urllib.parse
import urllib.request
import http.cookiejar
import login # Yazdigimiz kodu importluyoruz
import ssl

login.scraper_login() # Yazdigimiz kodu cagriyoruz giris yapmasi icin

ssl._create_default_https_context = ssl._create_unverified_context # Sertifika sorununu cozen sihirli satir

url = "https://arionline.ariokullari.k12.tr/course/view.php?id=232" # Mat dersi linki

# Dersi indiriyoruz
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
contents = response.read()

# Dersi 'arionline.html' dosyasina kaydediyoruz
f = open('arionline.html', 'wb')
f.write(contents)
f.close
