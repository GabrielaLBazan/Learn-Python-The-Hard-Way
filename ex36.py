from sys import exit

def focus_room():
    print "This is not really a room, obviously."
    print "It exists as a place to gather your thoughts... focus."
    raw_input("Type 'ready'> ")

    print "Let's workout to get the day started. (Option 1)"
    print "Or are we going straight to job applications? (Option 2)"
    print "Maybe we should just study. (Option 3)"

    choice = raw_input("Type 1, 2, or 3> ")
    if choice == '1':
        workout()
        return workout

    elif choice == '2':
        apply_for_jobs()
        return apply_for_jobs

    elif choice == '3':
        training()
        return training

    else:
        print "Maybe you need some more time to focus."



def workout():
    print "Did you go for the burn?"

    burn = raw_input("Yes/No> ")
    if "Yes" in burn:
        print "Good job! Let's get refocused"
        focus_room()

    elif "No" in burn:
        print "Get on it!"
        workout()

    else:
        print "Maybe you need some more time to focus."
        focus_room()


def apply_for_jobs():
    print "It's probably a good idea to get something sooner than later."
    print "Software Testing is fun!"
    print "You're not gonna stop doing your coding stuff are you?"

    coding = raw_input("> ")
    if "No" in coding:
        print "Good, let's get back on that."
        focus_room()

    else:
        print "Don't give up dude. You've come too far to stop. Do this for you!"
        print "You're not gonna really stop are you?"

        no_code = raw_input("> ")
        if "No" in no_code:
            print "That's more like it!"
            focus_room()

        elif "Yes" in no_code:
            print "Maybe you just need a break, but let's try to push through anyway."
            focus_room()

        else:
            print "Decide, yes or no!"
            print "Hint, stopping is not actually an option."
            apply_for_jobs()


def training():
    print "It won't be easy, it won't be fast, but it will be worth it."
    print "Let's start with Python and move to Free Code Camp after."
    print "Unless there's a different order preferred.  Pick Python or FCC."

    path = raw_input("> ")
    if "Python" in path:
        print "Let's 'Learn Python The Hard Way' shall we?"
        python()

    elif "FCC" in path:
        print "Let's go to camp, shall we?"
        fcc()

    else:
        print "pick Python or FCC"
        training()


def python():
    print "Stick with it and you'll finish.  This will help you understand so much more!"
    print "When you're done, let's do Free Code Camp stuff."
    raw_input("Type 'ready'> ")
    training()


def fcc():
    print "This is tough stuff, but you'll get it."
    print "Stick with it. did you finish the Python stuff already?"
    python_complete = raw_input("Yes/No> ")

    if "Yes" in python_complete:
        print "Good work! Let's get this career amped up!"
        career_choice()

    elif "No" in python_complete:
        print "Well, let's go back and do that."
        python()

    else:
        print "Yes or no, it's not hard to figure out."
        fcc()


def career_choice():
    print "Now we must decide, will you stick with the testing side?"
    print "Or will you officially cross over to the dark side and be a programmer?"
    career_path = raw_input("Tester or Programmer?> ")

    if "Tester" in career_path:
        print "Congratulations!  Now let's make that cashish!"
        exit()

    if "Programmer" in career_path:
        print "Ok, let's do this freelance style!  Make that money, honey!"
        exit()


focus_room()
