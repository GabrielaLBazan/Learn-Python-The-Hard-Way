# These are defining the variables x, binary, do_not, and y
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# This is a call to action, print x and print y, this will print the definitions above
print x
print y

# This is a call to action again, but with the insertion of the variable using string formats
print "I said %r." % x # r - raw string
print "I also said: '%s'." % y # s - string

# This is defining hilarious and joke_evaluation
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# This is a call to action to print to the screen the joke_evaluation with the hilarious definitions
print joke_evaluation % hilarious

# This is defining w and e
w = "This is the left side of..."
e = "a string with a right side."

# This is telling e to print after w
print w + e
