import calendar
from datetime import datetime

calendar.setfirstweekday(calendar.MONDAY)

inputUser = ""
while inputUser != "exit":
    print("0:Monday\n1:Tuesday\n2:Wednesday\n3:Thursday\n4:Friday\n5:Saturday\n6:Sunday\n")
    try:
        year = input("Enter Year:")
        if year == "exit":
            inputUser = "exit"
            break
        year=int(year)
        mon = int(input("Enter month 1-12:"))
        day = input("Enter weekday between 0-6 to select:")
        #print(list(calendar.monthrange(int(year), int(mon))))

        if int(day) not in [0, 1, 2, 3, 4, 5, 6]:
            raise ValueError("Invalid weekday value")

    except ValueError as e:
        print(str(e))
        continue

    count = 0
    for i in range(1, list(calendar.monthrange(int(year), int(mon)))[1]+1):
        if calendar.weekday(int(year), int(mon), i) == int(day):
            count += 1

    print(f"There are {count} {calendar.day_name[int(day)]}s in {calendar.month_name[int(mon)]} {year}")
