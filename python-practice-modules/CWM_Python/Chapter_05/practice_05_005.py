# Lecture on adding or removing items

letters = ["a", "b", "c"]

# to add
# letters.append("d")
# print(letters)

# to insert
# letters.insert(0, "-")
# print(letters)

# to remove something at the end of the list, use the pop method
# letters.pop()
# print(letters)

# to remove something within a list, specify the list number
# letters.pop(2)
# print(letters)

# to remove something where the index isn't known, use the remove method
# letters.remove("b")
# print(letters)

# we can also use the delete statement
# del letters[0:2]
# print(letters)

# to clear out the entire list, use the clear method
letters.clear()
print(letters)
