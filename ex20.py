# pulling the argument from the system
from sys import argv

# defining what belongs in the argument
script, input_file = argv

# defining the function "print_all" by making it read f (file) and then printing to the screen
# what when the f (file) is read
def print_all(f):
    print f.read()

# defining what the function "rewind"  the f (file) means by making the f (file) "seek"
# the beginning or line "0"
def rewind(f):
    f.seek(0)

# defining the function "print_a_line" by telling it to do a "line_count" of the "f" (file)
# then calling the action of "print" to screen the line_count from the file, by "read"ing
# each "line" (This adds the numbers to each line after the rewind)
def print_a_line(line_count, f):
    print line_count, f.readline()

# this defines the "current_file" as the open file that was entered from the argument in our
# original statement (line 5) EXAMPLE: "python ex20.py text2.txt"
current_file = open(input_file)

# this makes the words in quotes print to the screen - and makes a "\n"ew line
print "First let's print the whole file:\n"

# this says what to print after, "print_all" as defined above and calls on the "current_file"
# action as defined in line 25
print_all(current_file)

# again, print to screen the words in quotes
print "Now let's rewind, kind of like a tape."

# then calls the "rewind" function as defined above to go to line 0
rewind(current_file)

# print to screen the words in quotes
print "Let's print three lines:"

# this provides a number to start the numbering of the lines by defining current_line as 1
current_line = 1
# this tells python to print the first line, and that it is the line from the file
print_a_line(current_line, current_file)

# This defines the number for the next line by adding 1 to the line we're on and making that 2
current_line += 1 # this was modified to be simpler (same as line 54 just written differently)
# again, we're having python print the next line we're on from the line and file as instructed
print_a_line(current_line, current_file)

# defines the last number by again adding 1 to the last line we were on. line 2 + 1 = line 3
current_line = current_line + 1
# printing the next line we're on and pulling from current line and file
print_a_line(current_line, current_file)
