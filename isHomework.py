import urllib.parse
import urllib.request
import http.cookiejar
import ssl

ssl._create_default_https_context = ssl._create_unverified_context # Sertifika sorununu cozen sihirli satir

def findHomework(line, i):
    homework = ""
    for j in range(i - 133, 0, -1):
        if line[j] == '"':
            break
        homework += line[j]
    s = homework[::-1]
    homework = s
    return homework
def findHomeworkUrl(line, i):
    url = ""
    s = 'href="'
    for j in range(i, 0, -1):
        flag = 1
        for k in range(len(s)):
            if line[j + k] != s[k]:
                flag = 0
                break
        if flag == 1:
            for k in range(j + 6, j + 100):
                if line[k] == '"':
                    break
                url += line[k]
            break
    return url

def isHomework(url, name): # Odevi buluyor
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    contents = response.read()

    f = open(".files/" + name + ".html", 'wb')
    f.write(contents)
    f.close

    f = open(".files/" + name + '.html', 'r')
    lines = f.readlines()
    for line in lines:
        if "Tamamlanmadı" in line:
            for i in range(len(line)):
                s = 't="Tamamlanmadı;'
                flag = 1
                for j in range(len(s)):
                    if line[i + j] != s[j]:
                        flag = 0
                        break
                if flag == 1:
                    print(name + " odevin var! Odevin adi:", findHomework(line, i) + ".", "Odevin Linki:", findHomeworkUrl(line, i) + ".")
