import os
import sys
from art import tprint  #for ascii art
from logic import Hangman

game_over = False


def draw_hangman(number):
    # up to 6 wrong guesses
    # draws Hangman in 6 parts
    print()
    print('   +---+')  #row 1
    print('   |   |')  #row 2
    #row 3
    if number >= 1:
        print('   |   O')
    else:
        print('   |')
    #row 4
    if number >= 4:
        print('   |  /|\\')
    elif number >= 3:
        print('   |  /|')
    elif number >= 2:
        print('   |   |')
    else:
        print('   |')
    #row 5
    if number >= 6:
        print('   |  / \\')
    elif number >= 5:
        print('   |  /')
    else:
        print('   |')
    print('   |')  #row 6
    print(' =========')  #row 7


def clear_screen():
    '''
    Clear the Console/Terminal.
    '''
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')


hangman = Hangman()
while True:
    clear_screen()
    tprint('Hangman')
    print()
    print()
    for char in hangman.get_guessed_letters():
        print(char, ' ', end='')
    draw_hangman(hangman.get_number_guesses())
    print(f'Verbrauchte Buchstaben: {", ".join(hangman.get_used_letters())}')
    # get user guess
    guess = input("Buchstabe: ")
    #quit the game?
    if guess == '*':
        break
    hangman.make_guess(guess)
    # check if game lost
    if hangman.check_game_over() == 'game_lost':
        clear_screen()
        print()
        tprint('Verloren')
        print(f'Das Wort ist: {hangman.get_word()}')
        draw_hangman(hangman.get_number_guesses())
        game_over = True
        input('\nDrücke Enter zum fortfahren')
    # check if game won
    elif hangman.check_game_over() == 'game_won':
        clear_screen()
        print()
        tprint('Gewonnen')
        #print word
        for char in hangman.get_guessed_letters():
            print(char, ' ', end='')
        draw_hangman(hangman.get_number_guesses())
        game_over = True
        input('\nDrücke Enter zum fortfahren')

    if game_over:
        # reset hangman
        hangman.__init__()
        game_over = False
