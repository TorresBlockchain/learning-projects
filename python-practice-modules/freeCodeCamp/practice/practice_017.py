# Exercise on for loops

# for letter in "Torres Institute":
#     print(letter)

# this prints every letter in a loop

# below can also be used in arrays

# friends = ["Jim", "Karen", "Kevin"]
# for name in friends:
#     print(name)

# can also be used for numbers

# friends = ["Jim", "Karen", "Kevin"]
# for index in range(10): #it will not be including 10
#     print(index)


# friends = ["Jim", "Karen", "Kevin"]
# for index in range(4, 10):  # can also include a range
#     print(index)


# friends = ["Jim", "Karen", "Kevin"]
# len(friends) # to determine how big of an array this stores
# for index in range(len(friends)):
#     print(index)


friends = ["Jim", "Karen", "Kevin"]

for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print(index)
