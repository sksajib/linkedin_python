#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

# Errors can happen in programs, and we need a clean way to handle them
# TODO: This code will cause an error because you can't divide by zero:
#x=10/0
try:
    x-10/0
except:
    print("Math Exception")
# TODO: Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together
try:
    answer=input("What should i devide?")
    num=int(answer)
    print(10/num)
except ZeroDivisionError as e:
    print("Can't divide by Zero")
    print(e)
except ValueError as e:
    print("Need a number")
    print(e)
finally:
    print("Blah")

# TODO: You can also catch specific exceptions

