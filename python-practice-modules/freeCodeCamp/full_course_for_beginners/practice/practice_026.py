# Exercises on classes and objects

# class defines an overview
# object is an actual data point
# when using from command, it would look something as:
# from Student import Student
# even though they both reference student, they mean different things
# first student - refers to file
# second student - refers to class

class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
