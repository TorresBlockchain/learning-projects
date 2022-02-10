# Lesson on xargs

[2, 3, 4, 5]


# def multiply(*numbers):
#    for number in numbers:
#        total = total * number
#        total *= number


#multiply(2, 3, 4, 5)

# line 8 and 9 are the same operation

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
