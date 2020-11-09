import findCourses
import getTime
import sendMail
import isHomework

def sendHomework(info):
    tmp = findCourses.findCourses() # Ders ismini ve linkini aliyor
    names = tmp[0]
    links = tmp[1]

    if len(names) == 0 or len(links) == 0:
        print("Odevin yok!! Ya da bir hata var.")
        exit()

    homeworks = []

    for i in range(len(names)):
        messages = isHomework.isHomework(links[i], names[i]) # Her ders icin odev var mi diye kontrol ediyor

        for j in range(len(messages)):
            remaining_time = ""
            if 'assign' in messages[j][2]:
                remaining_time = getTime.remTime(messages[j][2], messages[j][1])
            else:
                remaining_time = "Sure yok"
            homeworks.append(messages[j][0] + " odevin var! Odevin adi: " + messages[j][1] + ". Odevin icin kalan sure: " + remaining_time + ". Odevin linki: " + messages[j][2] + ".")

    main_message = ""

    for i in range(len(homeworks)):
        main_message += homeworks[i]
        main_message += '\n';

    sendMail.send_mail("Odevlerin var!", main_message, info['recever_mail'], info['sender_mail'], info['sender_pass'])
