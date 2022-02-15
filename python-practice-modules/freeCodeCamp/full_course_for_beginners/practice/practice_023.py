# Exercise in reading files

# one can read and/or write into documents from python
# r - read
# w - write
# a - add new information
# r+ - read and writing
# anytime we open a file, we need to also add a command to close it at some point
# always make sure to store the data into a variable

# employee_file = open("practice_023.txt", "r")

# print(employee_file.read())

# employee_file.close()


# print(employee_file.readable()) #its a boolean order, show's if the file can be read or not
# print(employee_file.readline())
# to read multiple lines, it automatically goes to the next one when used multiple times
# print(employee_file.readline())
# print(employee_file.readlines()) #by using this command, it prints multiple lines and places them inside of an array
# print(employee_file.readlines()[1]) # used to read specific lines


employee_file = open("practice_023.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()


# employee_file = open("practice_023.txt", "r")
# print(employee_file.readlines()[2])
# employee_file.close()
