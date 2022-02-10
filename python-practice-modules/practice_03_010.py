# Lessons on while loops

#number = 100
# while number > 0:
#    print(number)
#    number = number // 2

# number //= 2 is the same as in line 6

#command = ""
# while command != "quit":
#    command = input(">")
#    print("ECHO", command)

# with the following code, one can eliminate the chance of input not being lower case

#command = ""
# while command != "quit" and command != "QUIT":
#    command = input(">")
#    print("ECHO", command)

# however, that does eliminate all possibilities of how the command in input
# in order to fix that, we use the following code

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
