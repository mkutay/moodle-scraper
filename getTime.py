import urllib.parse
import urllib.request
import http.cookiejar
import ssl

ssl._create_default_https_context = ssl._create_unverified_context # Sertifika sorununu cozen sihirli satir

def remTime(link, name):
    request = urllib.request.Request(link)
    response = urllib.request.urlopen(request)
    contents = response.read()

    f = open('.files/' + name + '.html', 'wb')
    f.write(contents)
    f.close

    remTime = ""

    f = open('.files/' + name + '.html', 'r')
    lines = f.readlines()
    for i in range(len(lines)):
        s = 'Kalan süre'
        if s in lines[i]:
            for j in range(37, len(lines[i + 1])):
                if lines[i + 1][j] == '<':
                    break
                remTime += lines[i + 1][j]
    f.close
    return remTime
