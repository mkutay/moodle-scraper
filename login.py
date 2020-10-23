import urllib.parse
import urllib.request
import http.cookiejar
import ssl

def scraper_login():
    ssl._create_default_https_context = ssl._create_unverified_context # Sertifika sorununu cozen sihirli satir

    base_url = 'arionline.ariokullari.k12.tr' # Sitenin asil url'si
    https_base_url = 'https://' + base_url # Sitenin asil url'si ile https'yi birlestiriyor

    # Bu da login'in oldugu yer
    authentication_url = https_base_url + '/login/index.php'

    username = '' # Kullanici adini girin
    password = '' # Sifreyi girin

    check_string = 'logout' # Bunu en sonda giris yapip yapmadigimiz kontrol etmek icin kullanacagiz

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
        'Referer': 'https://arionline.ariokullari.k12.tr/login/index.php',
        'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    } # Giris yaparken kullanacagimiz seyler

    # Cookie Jar'i baslatiyor
    cookie_jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
    urllib.request.install_opener(opener)

    # Logintoken'i almak icin giris sayfasini aliyoruz
    request = urllib.request.Request(https_base_url)
    response = urllib.request.urlopen(request)
    contents = response.read()

    logintoken = "" # Logintoken'i buna kaydedecegiz

    # Giris ekranindan aldiklarimizi "arionline.html" dosyasina kaydediyoruz
    f = open('.files/arionline.html', 'wb')
    f.write(contents)
    f.close

    f = open('.files/arionline.html', 'r')
    # Dosyaya kaydekttiklerimizden login token olana bakiyoruz ve logintoken'u aliyoruz
    line = f.readlines()
    for l in line:
        if "logintoken" in l:
            for i in range(len(l)):
                if l[i] == 'v':
                    for j in range(i + 7, len(l)):
                        if l[j] == '"':
                            break
                        logintoken += l[j]
    f.close

    payload = {
        'logintoken': logintoken,
        'username': username,
        'password': password
    } # Kullanici adinin, sifrenin ve logintokenin kayitli oldugu dictinory

    # Byte'larla gondereegiz bilgileri. Onun icin hazirlik yapiyoruz
    data = urllib.parse.urlencode(payload)
    binary_data = data.encode('UTF-8')

    # Gonderimi yapiyoruz 
    request = urllib.request.Request(authentication_url, binary_data, headers)
    response = urllib.request.urlopen(request)
    contents = response.read() # Giris yaptiktan sonraki sayfayi aliyoruz

    contents = contents.decode("utf-8")
    index = contents.find(check_string) # Sayfada giris yapip yapmadigimizi kontrol etmek icin kullandigimiz stringe bakiyoruz
    if index != -1: # Varsa buraya giriyor
        print("Login succesfull")
    else: # Yoksa buraya giriyor
        print("Login unsuccesfull")
