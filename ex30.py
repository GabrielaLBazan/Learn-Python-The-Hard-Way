# This block defines the amount of each set of objects
people = 30
cars = 40
trucks = 15

# This "if-statement" checks if the number of cars is greater than the number of people
if cars > people:
#  cars = 40 & people = 30 so this will be the statement we print
    print "We should take the cars."
# This "elif-statement" checks if the number of people is greater than the number of cars
elif cars < people:
# cars = 40 & people = 30 so this will NOT be the statement we print
    print "We should not take the cars."
# "else" says basically, any other outcome will print this statement (example cars == people)
else:
    print "We can't decide."

# This "if-statement" checks if the number of trucks is greater than the number of cars
if trucks > cars:
# trucks = 15 & cars = 40 so this will NOT be the statement we print
    print "That's too many trucks."
# This "elif-statement" checks if the number of cars is greater than the number of trucks
elif trucks < cars:
# trucks = 15 and cars = 40 so this WILL be the statement we print
    print "Maybe we could take the trucks."
# "else" says any other outcome, print "We still can't decide." (trucks == cars)
else:
    print "We still can't decide."
# This "if-statement" checks if the number of people is greater than the number of trucks
if people > trucks:
# people = 30 & trucks = 15, so this statement will work just fine for this comparison
    print "Alright, let's just take the trucks."
# "else" says if the trucks are greater or equal, then print "Fine, let's stay home then"
else:
    print "Fine, let's stay home then."
