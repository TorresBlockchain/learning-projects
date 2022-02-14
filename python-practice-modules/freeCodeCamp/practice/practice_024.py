# Exercise in writing files

# will append the file, will use "a" to add another employee into the file

# employee_file = open("practice_024.txt", "a")
# employee_file.write("Toby - Human Resources")
# employee_file.close()

# by using the code above, it added the new entry to the file, but added in the same row as the last one if there isn't a new line already

# employee_file = open("practice_024.txt", "a")
# employee_file.write("\nToby - Human Resources")
# employee_file.close()

# careful when editing files, by using 'w' instead of 'a', one can mistakenly overwrite an entire file

# we can even create new files through this command, by using the same code and changing the name of the file within

employee_file = open("practice_024_01.txt", "w")
employee_file.write("New file to save employee information")
employee_file.close()
