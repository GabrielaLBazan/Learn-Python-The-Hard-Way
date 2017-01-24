# Define (def) function "cheese_and_crackers" which means "cheese_count", then "boxes_of_crackers"
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count # %d asks for which variable, followed by identifying variable
    print "You have %d boxes of crackers!" % boxes_of_crackers # same as above
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# This prints the first line then completes the rest by calling on the function.
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30) # The function provides the variable argument amounts

# This calls for the function to reidentify variables into respective places
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
# where the defined function says cheese_count, boxes_of_crackers this matches those to
# amount_of_cheese, amount_of_crackers in that order respoectively
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)  # paying attention to the comma identifies which variable is for what.

# The amounts for amount_of_cheese and amount_of_crackers have been identified above,
# this adds the integers added with the '+' - again note the comma
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
