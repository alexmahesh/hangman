import random
from words import words

class Hangman:

    def __init__(self):
        self.word = random.choice(words)
        self.guessed_letters = []
        for _ in range(len(self.word)):
            self.guessed_letters.append('_')
        self.number_guesses = 0
        self.game_over = False
        self.used_letters = []
        self.max_guesses = 6

    def adapt_guessed_letters(self, letter):
        for i in range(len(self.word)):
            if self.word[i].lower() == letter.lower():
                self.guessed_letters[i] = letter

    def get_number_guesses(self):
      return self.number_guesses

    def get_word(self):
      return self.word

    def get_guessed_letters(self):
      return self.guessed_letters

    def get_used_letters(self):
      return self.used_letters

    def make_guess(self, guess):
        if guess.lower() in self.word.lower():
            self.adapt_guessed_letters(guess)
        else:
            self.number_guesses += 1
        if not guess.lower() in self.used_letters:
            self.used_letters.append(guess.lower())

    def check_game_over(self):
        if self.number_guesses >= self.max_guesses:
            return 'game_lost'
        elif self.word.lower() == ''.join(self.guessed_letters).lower():
            return 'game_won'
        else:
            return False
