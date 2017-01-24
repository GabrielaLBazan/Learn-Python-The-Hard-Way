def break_words(stuff):
    """This function will break up words for us.""" # Documentation Comments
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words.""" # Documentation Comments
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off.""" # Documentation Comments
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off.""" # Documentation Comments
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words.""" # Documentation Comments
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence.""" # Documentation Comments
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one.""" # Documentation Comments
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
