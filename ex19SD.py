def Gabi_and_Mel(dogs, kids):
    print "Gabi has %d dogs." % dogs
    print "Mel has %d kids." % kids
    print "That makes for a lot of chicken!"
    print "Good thing everyone gets along... usually\n"

print "Let's see if I've got this function thing down."
Gabi_and_Mel(1, 5)


print "How about redefining the variables."
amount_of_pups = 1
amount_of_kiddos = 5

Gabi_and_Mel(amount_of_pups, amount_of_kiddos)


print "What if we tried adding numbers for variable?"
Gabi_and_Mel(1 + 2, 5 + 4)

print "Adding numbers and variables, works just fine... in theory, not in real life."
Gabi_and_Mel(amount_of_pups + 2, amount_of_kiddos + 10)

print "I'm gonna get some more practice with calling these variables into the function."
print "How about weird math stuff like function adding to each other."
Gabi_and_Mel(1, 5), Gabi_and_Mel(1, 5)
