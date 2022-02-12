# learning on xxargs

def save_user(**user):
    print(user["age"])


save_user(id=1, name="John", age=22)

# what comes out of it, its called a dictionary
# by modifying what's inside the brakets on line 4 with quotations, it can select what from the dictionary gets printed in the terminal
# if you want to print the entire dictionary, remove the brakets and just leave as - print(user)
