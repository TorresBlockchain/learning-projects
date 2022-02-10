# Lesson on default arguments
# will be going over on how to make the by argument optional
# optional parameters should come after the required parameters

def increment(number, by=1):
    return number + by


print(increment(2, 5))
