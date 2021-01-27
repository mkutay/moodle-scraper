import os
import os.path
import sendMail

def check(homeworks, info):
    if os.path.isfile(".chomeworks") == False:
        f = open(".chomeworks", "w+")
        f.close()

    sendData = []

    for hw in homeworks:
        link = hw["url"]
        re = open(".chomeworks", "r")
        lines = re.readlines()
        flag = False
        for line in lines:
            # print(line.rstrip("\n"))
            # print("link = \"" + link + "\", line = \"" + line.rstrip("\n") + "\"")
            if line.rstrip("\n") == link:
                flag = True
                break
        if flag == True:
            continue

        sendData.append(hw)

        re.close()

        wr = open(".chomeworks", "a+")
        wr.write(link + "\n")
        wr.close()

    if len(sendData) == 0:
        print("All homeworks were checked before, exiting")
        return

    main_message = ""
    for i in range(len(sendData)):
        main_message += sendData[i]["className"] + "dersinde odevin var. " + "Odevin adi " + sendData[i]["homeworkName"] + ". Odevin icin Kalan sure " + sendData[i]["remTime"] + ". Odevin linki " + sendData[i]["url"] + "."
        main_message += "\n"

    sendMail.send_mail("Yeni Odevlerin Var", main_message, info['recever_mail'], info['sender_mail'], info['sender_pass'])
