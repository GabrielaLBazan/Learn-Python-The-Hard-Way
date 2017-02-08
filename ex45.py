from sys import exit



class Scene(object):

    def enter(self):
        print "This doesn't really need anything, it's a place holder for scenes"
        exit(1)


class Home(object):

    def __init__(self, scene_plan):
        self.scene_plan = scene_plan

    def play(self):
        current_scene = self.scene_plan.opening_scene()
        last_scene = self.scene_plan.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_plan.next_scene(next_scene_name)

        current_scene.enter()


class Bedroom(Scene):

    quips = [
        "Normally going to your bedroom would be considered a good thing.",
        "Looks like you're gonna have to just dream about a better night this time.",
        "It's like you want to sleep alone, what the heck?",
        "Do you think this is really good for your relationship?",
        "Way to go dummy, you messed that one up.",
        "For being the master, you sure haven't mastered anything out of the bedroom."
    ]

    def enter(self):
        print Bedroom.quips[randint(0, len(self.quips)-1)]
        exit(1)

class Restaurant(Scene):
    def enter(self):
        print "Look at you two, out on the town like a couple of grown ups!"
        print "It's been a while since you've had an actual date, isn't it nice?"
        print "Never forget what this is like because it will hold you over till"
        print "the next time."
        print "Think you have time for a movie too?"
        movie = raw_input("yes/no> ")

        if movie == "yes":
            print "Well this is a treat!"
            print "Don't forget to turn off your ringers in the theater when you"
            print "get over there!"
            return 'movie_theater'
        else:
            print "That's alright, at least you had time for a nice dinner together."
            print "She's got a lot on her plate and all you do is sit at your desks"
            print "coding stuff and making games.  But they work don't they? haha!"
            print "Don't forget to thank her for taking a little extra time to spend"
            print "with you tonight."
            return 'end_of_date'

class MovieTheater(Scene):
    def enter(self):
        print "Finally, a whole date night; movie, dinner and the two of you."
        print "It's always nice to be around everyone (when they're in a good mood)"
        print "but time together is really nice too.  Grown ups talking about grown"
        print "up stuff without a filter."
        print "Hold on to moments like these.  They'll get you through the tough"
        print "days."
        return 'end_of_date'

class Car(Scene):
    def enter(self):
        print "Just another day in the life of the Mel and Gabi show."
        print "Each day is a new adventure, it's completely up to you if you make it"
        print "to a nice date with the 'Eff Dub'.  Play your cards right and you get"
        print "dinner and a movie with the lovely Miss Mel.  But if you don't play"
        print "right, you may end up on errand mode, or worse, you'll end up at home"
        print "she'll take the kids to run errands and you'll be in your bedroom."
        print "The bedroom that feels so cold and lonely when you two are fighting."
        print "So good luck and don't f*ck it up!"
        print "\n"
        print "You manage to wake up with your alarm instead of sleeping in today, so"
        print "let's make it a productive day."
        print "Go running and get some endorphins running through you so you can be"
        print " in a good mood and not piss anyone off.  And by anyone... you know"
        print "who that means."
        print "Did you run?"
        run = raw_input("yes/no> ")

        if run == "yes":
            print "We're off to a great start!  Let's hope your positive mood is "
            print "welcomed and you're invited to participate in today's activities."
            return 'target'
        elif run == "no":
            print "Uh oh, well, let's hope you slept in a little and cuddled so "
            print "the good feelings are running through you."
            print "be aware that you may be a little low on energy and happy feelings"
            return 'grocery_store'
        else:
            print "DO NOT UNDERSTAND WHAT YOU'RE SAYING"
            return 'car'

class GroceryStore(Scene):
    def enter(self):
        print "You made it on an errand, that's the good news.  The bad news,"
        print "It's the first of the month and you're at WalMart.  Let's just hope"
        print "this goes well."
        print "\n"
        print "Since wer're at this wretched place, maybe you should hint at another"
        print "date night.  You won't have another chance to be alone, let her worry"
        print "about what your alibi is for tonight."
        return date_night()



class Target(Scene):
    def enter(self):
        print "Target time!"
        print "Well, you were included on this outting, and it's not WalMart, so"
        print "looks like you're on the right track for the day."
        print "If everyone went to school today, you might not have to rush home."
        print "Did everyone go to school today?"
        attendance = raw_input("yes/no> ")

        if attendance == "yes":
            print "In that case, maybe you should drop the hint about a date night/day"
            print "whatever time of the day, just make sure you set the time so it"
            print "can't just be another thing you don't plan and then don't do."
            print "It can't hurt to ask her for a date night right?"
            print "You can either drop a hint or keep quiet."
            return date_night()

        elif attendance == "no":
            print "That's a bummer, you'll definitely have to figure out if a date"
            print "is even possible at all today based on who's sick or what's wrong."
            print "Who's home?"
            home_sick = raw_input("> ")

            if home_sick == "Rowan":
                print "She's too young to stay home alone.  Is Quadry home?"
                quadry = raw_input("yes/no> ")

                if quadry == "yes":
                    print "Well, it might still be alright if he can watch her."
                    print "maybe you can discuss more a little later."
                    return 'grocery_store'
                else:
                    print "Guess that means we can't do much without someone to watch her."
                    print "Next time."
                    print "Shouldn't really get mad, but you can't help but hope for more"
                    print "time alone.  Just the luck of the draw."
                    return 'bedroom'

            else:
                print "Well they're ok alone, they can take care of themselves for the most"
                print "part. Let's see how the day goes and we'll go from there."
                return 'grocery_store'

        else:
            print "Maybe you should rethink and keep going with your day if you don't"
            print "know where the kids are today."
            return 'grocery_store'


class EndOfDate(Scene):
    def enter(self):
        print "End of Date scene works"

class Finished(Scene):
    def enter(self):
        print "All in a days work."
        return 'finished'


class Plan(object):

    scenes = {
        'car': Car(),
        'grocery_store': GroceryStore(),
        'target': Target(),
        'restaurant': Restaurant(),
        'movie_theater': MovieTheater(),
        'bedroom': Bedroom(),
        'end_of_date': EndOfDate(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Plan.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

def date_night():
    date_tonight = False
    while True:
        date = raw_input("hint/quiet> ")

        if date == "hint":
            print "There you go!  You dropped your hint.  You did your part."
            print "What did she say?"
            response = raw_input("yes/no/maybe> ")

            if response == "yes":
                print "Yay! better start making the plans.  Don't want this"
                print "chance to get away."
                date_tonight = True
                return 'restaurant'
            elif response == "no":
                print "Well maybe next time, don't make a sad face.  She'll"
                print "get in a bad mood too and you'll not get to enjoy"
                print "more time with her."
                return 'grocery_store'
            else:
                print "That indecisiveness may be something else.  Or she"
                print "might have something to do later and isn't quite sure."
                print "It's all about how you respond.  Maybe there's a"
                print "compromise you can make."
                print "Can you calm down a little? Press enter to continue."
                raw_input("> ")
                print "Uh oh, this feels like you might get into a fight."
                print "You couldn't just stay positive and avoid this?"
                return 'bedroom'

        elif date == "quiet":
            print "Well, you can be quiet for now, but don't let that go for"
            print "too long, it's not something you want to keep inside and"
            print "then miss out on."
            return 'grocery_store'

        else:
            print "Let's try this again, since you can't pick hint or quiet."
            return date_night()


a_plan = Plan('car')
a_game = Home(a_plan)
a_game.play()
