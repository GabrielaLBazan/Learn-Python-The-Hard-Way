from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):
        ## listing the quips that will be called in the function below
        quips = [
            "Well, well, well, doesn't look like you made it this time.",
            "Does it always work out this way for you?",
            "There are better things to do than just play this game and die you know.",
            "Don't feel bad, no one can win this game, it's rigged... sorta."
        ]
        ## defining the function
        def enter(self):
            # print is the action, then we're calling "Death"class to run quips listed above
            # the parameters are in the brackets randint calls the random integer.
            # 0 pulls the first listed item, then from the length of the list call quips
            # then call the next one that wasn't the last one used (-1)
            print Death.quips[randint(0, len(self.quips)-1)]
            exit (1)



class CentralCorridor(Scene):

    def enter(self):
        print "You are in the Central Corridor."
        print "Apparently there are some things here called Gothons."
        print "So you have to get rid of those and get outta this place."
        print "\n"
        print "You can go across the bridge to place the bomb to destroy the Gothons."
        print "But you should probably go to the Laser Weapon Armory to get a neutron bomb."
        print "Ultimately, you want to get to the Escape Pod and get outta here."

        action = raw_input("> ")

        if action == "Cross Bridge":
            print "You aren't armed, are you sure?"
            cross = raw_input("Yes/No> ")
            if cross == "Yes":
                print "Ok, let's see how well this goes"
                return 'the_bridge'
            if cross == "No":
                print "We should probably go to the Armory, right?"
                return 'central_corridor'

        elif action == "Laser Weapon Armory":
            print "Let's get some guns and shoot stuff!"
            return 'laser_weapon_armory'

        else:
            print "Wrong answer, here come the Gothons!"
            print "It's too late, they've seen you and they're coming for you!"
            return 'death'



class LaserWeaponArmory(Scene):

    def enter(self):
        print "You made it to the 'gun show'!"
        print "Let's get some guns and if you want to blow this place up we're going to need"
        print "a bomb.  There may be one problem with the bomb."
        print "There might be a lock on it and you might not have the pin to the keypad."
        print "Enter 3 digits to try to unlock the bomb container."
        lock = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != lock and guesses <9:
            print "ERRRRRRR, WRONG!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == lock:
            print "Holy cow! You guessed the code!"
            print "Your jedi mind tricks worked and you can get the bomb to throw at the"
            print "Gothons.  Get that bomb and get the heck outta here."
            print "Head to the bridge to place the bomb!"
            return 'the_bridge'

        else:
            print "That's incorrect! You're in for a world of hurt."
            print "The room locks shut and you can't find anyway out of this place!"
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print "You see a Gothon on the Bridge."
        print "You must get past him to get to the Escape Pod."
        print "Choose to fight, tell a joke, or turn around and try another way."

        gothon = raw_input("Fight/Joke/Misc> ")

        if gothon == "Fight":
            print "Will you use a weapon or fight bare-handed?"
            weapon = raw_input("> ")

            if weapon == "weapon":
                print "Let's go to the Laser Weapon Armory first."
                raw_input ("Press Enter if Ok>")
                return 'central_corridor'

            elif weapon == "bare-handed":
                print "Alright Rambo, let's do this!"
                return 'scene.death'

            else:
                print "You really think indecision is the right thing to do here?"
                return 'scene.death'

        if gothon =="Joke":
            print "You think you're funny don't you?"
            funny = raw_input("Yes/No> ")

            if funny == "Yes":
                print "Tell a joke then, it better be funny."
                raw_input("> ")
                print "That's a good one"
                print "You made it past the Gothon, heading to the escape pod is your only"
                print "chance to survive!"
                print "\n"
                return 'escape_pod'

            elif funny == "No":
                print "So you don't have a joke then? What a jip."
                return 'death'

            else:
                print "Your indecisiveness is concerning."
                return 'death'

        else:
            print "You're not funny and you can't fight..."
            print "There are much bigger problems here, obviously."
            return 'death'



class EscapePod(Scene):

    def enter(self):
        print "You've reached the Escape Pods, but there are 5 of them!"
        print "You must guess the correct pod to escape!"
        print "Hurry, pick a pod!"

        pod = randint(1,5)
        guess = raw_input("[pod #]> ")

        if int(guess) != pod:
            print "Oh no!"
            print "You couldn't just get in the pod?  You're stuck here now."
            print "What the hell is a Gothon anyway?"
            print "You're never gonna find out now, because you're dead!"
            return 'death'
        else:
            print "You got it!  Pod %s was the right one!" % guess
            print "Now get the hell outta here before those Gothons"
            print "catch up with you!"
            print "Congratulations on winning!"

            return 'finished'




class Finished(Scene):

    def enter(self):
        print "Yay! You won! Your reward? You don't have to play anymore, lucky you!"
        return 'finished'

class Map(object):

    scenes = {
    'the_bridge': TheBridge(),
    'laser_weapon_armory': LaserWeaponArmory(),
    'central_corridor': CentralCorridor(),
    'escape_pod': EscapePod(),
    'death': Death(),
    'finished': Finished()

    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
