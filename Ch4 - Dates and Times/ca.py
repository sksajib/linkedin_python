import calendar
calendar.setfirstweekday(calendar.MONDAY)
print(list(calendar.monthrange(2023,4))[1])