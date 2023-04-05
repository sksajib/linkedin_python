#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# TODO: construct a basic timedelta and print it

print(timedelta(days=365,hours=5,minutes=3))
# TODO: print today's date
now=datetime.now()

print("one year from now it will be",str(now+timedelta(days=365)))
print("In two weeks and 3 days it will be",str(now+timedelta(weeks=2,days=3)))

# TODO: print today's date one year from now


# TODO: create a timedelta that uses more than one argument


# TODO: calculate the date 1 week ago, formatted as a string


### How many days until April Fools' Day?


# TODO: use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year


# TODO: Now calculate the amount of time until April Fool's Day  

