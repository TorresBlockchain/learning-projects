# Exercise
# Conditions
# divisible by 3 - Fizz
# divisible by 5 - Buzz
# divisible by 5 & 3 - FizzBuzz
# any other number, return the user input

import numbers


def fizz_buzz(input):
    total = 1
    if numbers % 3 == 0:
        print("Fizz")
    elif numbers % 5 == 0:
        print("Buzz")
    elif numbers % 3 == 0:
        print("FizzBuzz")
    else:
        print(input)


print(fizz_buzz(3))
