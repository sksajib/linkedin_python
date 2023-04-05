#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#

from datetime import date
from datetime import time
from datetime import datetime


def main():
    ## DATE OBJECTS
    # TODO: Get today's date from the simple today() method from the date class
    today=date.today()
    print(today)

    # TODO: print out the date's individual components

    print("Date components: ",today.day, today.month,today.year)
    # TODO: retrieve today's weekday (0=Monday, 6=Sunday)

    print("todays weekday is: ",today.weekday()) 
    days=["mon","tuesday","wed","thrus","fri","sat","sun"]
    print("which is a ",days[today.weekday()])
    ## DATETIME OBJECTS
    today=datetime.now()
    print(today)
    t=datetime.time(datetime.now())
    print(t)
    # TODO: Get today's date from the datetime class

    
    # TODO: Get the current time

 

  
if __name__ == "__main__":
    main()
  