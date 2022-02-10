# Lessons on scope

message = "a"


def greet(name):
    global message
    message = "b"


greet("Omar")
print(message)
