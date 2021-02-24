import os
# main_message2.append(homeworks[i]["className"] + " dersinde odevin var. " + "Odevin adi " + homeworks[i]["homeworkName"] + ". Odevin icin Kalan sure " + homeworks[i]["remTime"] + ". Odevin linki " + homeworks[i]["url"] + ".")
def out(main_message, homeworks):
    f = """<!DOCTYPE html>
<html>
<head>
<title>Odevler</title>
</head>
<body>

<h1>Odevlerin Var!</h1>
"""
    with open("output.html", "w") as outfile:
        for i in range(len(main_message)):
            link = "<a href=\"" + homeworks[i]["url"] + "\" target=\"_blank\">Odevin linki</a>"
            msg = homeworks[i]["className"] + " dersinde odevin var. " + "Odevin adi " + homeworks[i]["homeworkName"] + ". Odevin icin Kalan sure " + homeworks[i]["remTime"] + ". " + link + ".\n"
            f += "<p>" + msg + "</p>\n"
        f += """</body>
</html>
"""
        outfile.write(f)
    os.system("open output.html")
