import random

class Hangman:
    def __init__(self, word_list):
        self.word_list = word_list
        self.secret_word = random.choice(self.word_list).upper()
        self.guesses_left = 6
        self.guessed_letters = set()
        self.display_word = ['_'] * len(self.secret_word)

    def display_game_status(self):
        print("Word:", " ".join(self.display_word))
        print("Guesses left:", self.guesses_left)
        print("Guessed letters:", " ".join(sorted(self.guessed_letters)))

    def guess(self, letter):
        if letter.upper() in self.guessed_letters:
            print("You've already guessed that letter.")
            return

        self.guessed_letters.add(letter.upper())

        if letter.upper() in self.secret_word:
            for i, char in enumerate(self.secret_word):
                if char == letter.upper():
                    self.display_word[i] = char
        else:
            self.guesses_left -= 1

    def check_game_over(self):
        if '_' not in self.display_word:
            print("Congratulations! You've guessed the word:", self.secret_word)
            return True
        elif self.guesses_left == 0:
            print("Game over! The word was:", self.secret_word)
            return True
        return False

# Example usage:
word_list = ["python", "hangman", "programming", "computer", "game"]
game = Hangman(word_list)

print("Welcome to Hangman!")
game.display_game_status()

while not game.check_game_over():
    letter = input("Guess a letter: ")
    game.guess(letter)
    game.display_game_status()