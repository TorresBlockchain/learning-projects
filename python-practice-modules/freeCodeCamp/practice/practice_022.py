# Exercises on try/except errors

# number = int(input("Enter a number"))
# print(number)

# program will work good as long as an integer is placed inside,
# but we need to start having solutions when that doesn't happen

# try:
#     number = int(input("Enter a number"))
#     print(number)
# except:
#     print("Invalid Input")

# this program is able to return any integer value, however if anything else is placed inside, it'll return the stated error

# we can be more detailed by also having various except print out when stated

try:
    number = int(input("Enter a number "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid Input")

# when using the except function, usually have various outcomes, leaving just one is too broad
