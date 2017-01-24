# call to action to run the module sys and import the argument values (these are entered when
# the user is running the command in python)
from sys import argv

# This lists the number of argument values there are and what they are, script is the file name
# [.py] run after "python" in Powershell and filename is the txt file made for this exercise
script, filename = argv

# This is telling the txt to open the filename provided and labeling it txt
txt = open(filename)

# call to action to print to the screen "Here's your file" and the filename will be entered in %r
print "Here's your file %r:" % filename
# print to screen the txt read
print txt.read()

# print to screen the prompt to type the filename again
print "Type the filename again:"
# This defines the file name being repeated as file_again and gives a prompt for raw input
file_again = raw_input("> ")

# call for txt to open and read the file again while calling it txt_again
txt_again = open(file_again)

# this make the file that's re-read print on the screen
print txt_again.read()

txt.close()
txt_again.close()
