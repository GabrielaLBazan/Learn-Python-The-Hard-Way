class Tune(object):

    def __init__(self, words):
        self.words = words

    def lets_sing_a_song(self):
        for line in self.words:
            print line

i_adore_you = Tune(["Cuz everytime I see you",
                    "It's like all I am is see thru",
                    "We were everything I know it",
                    "Don't wanna miss it, record it"])

you_earned_it = Tune(["You make it look like it's magic, oh yeah",
                      "I'm never confused, hey hey",
                      "I'm so used to being used"])

i_adore_you.lets_sing_a_song()

you_earned_it.lets_sing_a_song()
