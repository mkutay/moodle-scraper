import urllib.parse
import urllib.request
import http.cookiejar
import ssl

def findCourseLink(line, i): # Eger ders varsa linkini buluyor ve geri donduruyor
    s = "Bu derse girmek için tıklayınız"
    flag = 1
    for j in range(len(s)):
        if line[i + j] != s[j]:
            flag = 0;
            break
    if flag == 1:
        knil = ""
        for j in range(i - 3, 0, -1):
            if line[j] == '"':
                break
            knil += line[j]
        link = knil[::-1]
        return link
    return -1

def findCourseName(line, link, i): # Link veriliyor ona gore o linkin dersini buluyor
    s = 'class="" href='
    for j in range(i, 0, -1):
        flag = 1
        for k in range(len(s)):
            if line[j + k] != s[k]:
                flag = 0
                break
        if flag == 1:
            name = ""
            for k in range(j + 17 + len(link), len(line)):
                if line[k] == '<':
                    break
                name += line[k]
            return name

def findCourses(): # Tum derslerin linkini ve adini buluyor
    ssl._create_default_https_context = ssl._create_unverified_context # Sertifika sorununu cozen sihirli satir

    url = "https://arionline.ariokullari.k12.tr/"

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    contents = response.read()

    f = open('.files/main.html', 'wb')
    f.write(contents)
    f.close

    f = open('.files/main.html', 'r')
    lines = f.readlines()
    names = []
    links = []
    for line in lines:
        for i in range(len(line)):
            link = findCourseLink(line, i)
            if link != -1:
                name = findCourseName(line, link, i)
                names.append(name)
                links.append(link)
    return [names, links] # returning them

