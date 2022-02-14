# Exercises on modules and pip

# this is good for having useful functions and information in other files in other programs, and not copy and pasting the information
# just import with the name of the file afterwards
# when wanting to use a specific function, print(name of the file.)
# after having the . within the print function, the program will give you a list of the items that can be used within python
# a module is an external file that you want to use to a program you are working on

import practice_025_reference

print(practice_025_reference.roll_dice(15))

# theres 3 types of modules
# created - those modules that you create and have stored in your directory
# internal - those modules that come integrated within python, those that are installed along with python in external libraries/lib
# external - one has to bring these in to be used within python (third party)
# google python third party modules to see useful ones that come over
# this is where pip comes in, where we can install 3rd party module, its a package manager
# in updated python, its already pre-installed
# downloaded the docx module, its located on windowstore folder in python tab under packages
# to uninstall any module downloaded, use the following code: pip uninstall python-docx
