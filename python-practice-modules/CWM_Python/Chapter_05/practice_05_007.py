# Lecture on sorting lists

# this method of sorts from bottom to highest
# numbers = [3, 51, 2, 8, 6]
# numbers.sort()
# print(numbers)

# in order to do it in decending order, will need to do the following
# numbers = [3, 51, 2, 8, 6]
# numbers.sort(reverse=True)
# print(numbers)

# A quicker code in order to have it sorted, would be the following as well in reverse
numbers = [3, 51, 2, 8, 6]
print(sorted(numbers))
print(sorted(numbers, reverse=True))
