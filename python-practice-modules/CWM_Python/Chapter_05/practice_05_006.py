# Lecture in finding items

# when attempting to print an item that doesn't exist, you'll get an error on python
# however, one can check in other ways
# letters = ["a", "b", "c"]
# print(letters.index("d"))


# letters = ["a", "b", "c"]
# if "d" in letters: # since we included an if statement, it will not give us an error now
#     print(letters.index("d"))

# on this one, with the count method, it will give us the amount of times the specific data point comes up in the list
letters = ["a", "b", "c"]
print(letters.count("d"))
if "d" in letters:
    print(letters.index("d"))
