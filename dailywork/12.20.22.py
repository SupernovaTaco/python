import os
import getpass
clear = lambda: os.system('cls')

class hangman:
    word = None
    used_letters = None
    wrong_choices = None
    word_guesses = None
    in_progress = True

    def __init__(this, word, used_letters, wrong_choices, word_guesses, in_progress):
        this.word = word
        this.used_letters = used_letters
        this.wrong_choices = wrong_choices
        this.word_guesses = word_guesses
        this.in_progress = in_progress
    
    def start(this):
        while this.in_progress:
            print('hello world')
def get_game_phrase():
    valid_phrase = ' '
    while len(valid_phrase) <= 0:
        phrase = getpass.getpass('please proivide a word or phrase to get started: ')
        verify = getpass.getpass('please verify your word or phrase: ')
        if phrase == verify:
            valid_phrase = verify
        else:
            print('oops! your answers didnt match, please try again\n')
    return valid_phrase



game_phrase = get_game_phrase()
game = hangman(game_phrase)
game.start()

