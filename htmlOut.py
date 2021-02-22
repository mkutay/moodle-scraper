import os
def out(main_message):
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
            f += "<p>" + main_message[i] + "</p>\n"
        f += """</body>
</html>
"""
        outfile.write(f)
    os.system("open output.html")
