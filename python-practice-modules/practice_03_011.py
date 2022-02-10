# Lessons on infinite loops

# issue with infinite loop is if one does not have a way to break out of the cycle
# we risk in consuming all the memory causing the program to crash

command = ""
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
