def taketime(time):
    timelist = []
    timestr = str()
    for i in time:
        if i != ":" and i != " ":
            timestr = timestr + i
        else:
            timelist = timelist + [timestr]
            timestr = str()
    timelist = timelist + [timestr]
    return timelist


def add_time(time1, time2, day=False):
    time1list = taketime(time1)
    time2list = taketime(time2)
    timesum1 = int(time1list[0]) + int(time2list[0])
    timesum2 = int(time1list[1]) + int(time2list[1])
    if timesum2 > 60:
        timesum1 = timesum1 + 1
        timesum2 = timesum2 - 60
    if timesum2 < 10:
        timesum2 = str("0") + str(timesum2)
    AMPM = time1list[2]
    dayspassed = False
    if int(str(timesum1) + str(timesum2)) > 1200:
        timepassed = timesum1 // 12
        if timesum1 > 24:
            if AMPM == "PM":
                dayspassed = (timesum1 + 12) // 24
            else:
                dayspassed = timesum1 // 24
        elif timesum1 > 12 and AMPM == "PM":
            dayspassed = 1
        AMPM = 1 if time1list[2] == "PM" else 0
        realAMPM = (AMPM + timepassed)%2
        AMPM = "AM" if realAMPM == 0 else "PM"
        timesum1 = timesum1 - 12*(timesum1//12)
    if timesum1 == 0:
        timesum1 = 12
    if day:
        day = day.upper()
        if not dayspassed:
            return str(timesum1) + ":" + str(timesum2) + " " + str(AMPM) + ", " + day.capitalize()
        else:
            daylist = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
            for i in range(len(daylist)):
                if day == daylist[i]:
                    day = i
            if dayspassed == 1:
                day = daylist[(day+1)%7]
                return str(timesum1) + ":" + str(timesum2) + " " + str(AMPM) + ", " + day.capitalize() + " (next day)"
            else:
                day = daylist[(day+dayspassed)%7]
                return str(timesum1) + ":" + str(timesum2) + " " + str(AMPM) + ", " + day.capitalize() + " (" + str(dayspassed) + " days later)"
    if not dayspassed:
        return str(timesum1) + ":" + str(timesum2) + " " + str(AMPM)
    else:
        if dayspassed == 1:
            return str(timesum1) + ":" + str(timesum2) + " " + str(AMPM) + " (next day)"
        else:
            return str(timesum1) + ":" + str(timesum2) + " " + str(AMPM) + " ("+ str(dayspassed) + " days later)"
