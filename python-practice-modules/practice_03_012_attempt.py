# Exercise on having an output of the following

# 2
# 4
# 6
# 8
# We have 4 even numbers

# Loops like a loop with the exercise where we also used steps
# that was on exercise practice_03_006
# edits will be to keep the limit to 8 and remove the extra items being printed in the other exercise
# once having the number coming out, will need to also add the last printed statement
# can't add print(statement) because its repeated after each iteration, will need some sort of if statement
# by adding the successful portion of practice_03_007, we were able to get the interation 2, now we need to extend for the other 3


#successful = 10
# for number in range(2, 10, 2):
#    if number < 10:
#        print(number)

#    if successful:
#        print("We have 4 even numbers")
#        break

successful = True
for x in [2, 4, 6, 8]:
    print(x)
    if successful:
        print(x)
        break
else:
    print("We have 4 even numbers")
