# Lesson on Logical Operators
# and
# or
# not

#high_income = True
#good_credit = True

# if high_income and good_credit:
#    print("Eligible")
# else:
#    print("Not Eligible")

#high_income = False
#good_credit = False

# if high_income or good_credit:
#   print("Eligible")
# else:
#   print("Not Eligible")

high_income = True
good_credit = True
student = False

# if not student:
#    print("Eligible")
# else:
#    print("Not Eligible")

high_income = True
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")
