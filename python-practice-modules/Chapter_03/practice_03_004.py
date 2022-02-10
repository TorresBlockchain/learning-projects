# Lesson on short-circuit evaluation

high_income = True
good_credit = True
student = True

if high_income and good_credit and not student:
    print("Eligible")
