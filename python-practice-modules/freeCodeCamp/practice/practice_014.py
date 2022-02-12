# Exercises on dictionaries

# when creating dictionaries in python, we always place the data inside {}
# will not allow you have duplicate keys

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions)
print(monthConversions["Nov"])  # will refer to the key when retriving it
print(monthConversions.get("Jun"))  # this will also do another retriving

# keys can also be numbers
