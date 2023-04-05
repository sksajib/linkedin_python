#
# Example file for formatting time and date output
# LinkedIn Learning Python course by Joe Marini
#


from datetime import datetime

def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes 
    now =datetime.now()

    print(now.strftime("The current year is: %Y"))
    print(now.strftime("%a, %d %B, %Y"))
    print(now.strftime("locate date:%x"))
    print(now.strftime("locate time:%X"))
    #### Date Formatting ####
    print(now.strftime("Current time : %I:%M:%S %p"))
    print(now.strftime("Current 24 hour time : %H:%M:%S "))
    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month


    # %c - locale's date and time, %x - locale's date, %X - locale's time


    #### Time Formatting ####
    
    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  

if __name__ == "__main__":
    main()
