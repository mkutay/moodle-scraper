import os
def out(main_message):
    with open("output.html", "w") as outfile:
        outfile.write(main_message)
    os.system("open output.html")
