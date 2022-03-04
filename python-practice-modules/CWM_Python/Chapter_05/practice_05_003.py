# Lecture on unpacking lists

# numbers = [1, 2, 3]
# first, second, third = numbers

# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# lines 3 - 4 represent the same as in lines 6-8
# whenever we do specify all the items to the left size of the equals in line 4, we'll get an error due to having too many things to unpack
# the way we go around that is by specifying what we need, and for everything else to be stored on *other

# numbers = [1, 2, 3, 4, 4, 4, 4, 4, 4, 4]
# first, second, *other = numbers
# print(first)
# print(second)
# print(other)

# you can also group lists and call out specific areas you want called
# in this example we only one the first and last items and everything in between can be stored in *other
numbers = [1, 2, 3, 4, 4, 4, 4, 4, 4, 9]
first, *other, last = numbers
print(first)
print(last)
print(first, last)
print(other)
