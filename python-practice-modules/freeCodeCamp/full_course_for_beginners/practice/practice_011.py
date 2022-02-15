# Exercises on if statements

# is_male = True

# if is_male:
#     print("You are a male")

# anything after the if statement, until broken, will use everything under that statement
# it will only print when its True
# if statement isn't true, it won't print anything

# is_male = False

# if is_male:
#     print("You are a male")
# else:
#     print("You are not a male")


# in order for something to print with False, there must be another output ready to post in else section
# if not, it will be empty as the previous example


# is_male = False
# is_tall = False

# if is_male or is_tall:
#     print("You are a male or tall or both")
# else:
#     print("You are neither male nor tall")

# one can also add various variables and use them along with and/or operators in if statements

is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a male or tall or both")
elif is_male and not (is_tall):
    print("You are a short male")
elif not(is_male) and (is_tall):
    print("You are a short male")
else:
    print("You are neither male nor tall")

# one can use the operator not, which does the opposite of whats inside the variable
