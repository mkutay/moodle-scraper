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
            mp = {"className": messages[j][0], "homeworkName": messages[j][1], "remTime": remaining_time, "url": messages[j][2]}
            # homeworks.append(messages[j][0] + " odevin var! Odevin adi: " + messages[j][1] + ". Odevin icin kalan sure: " + remaining_time + ". Odevin linki: " + messages[j][2] + ".")
            homeworks.append(mp)

    return homeworks
