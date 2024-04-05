import random

class GuessTheNumber:
    def __init__(self, min_num, max_num):
        self.min_num = min_num
        self.max_num = max_num
        self.secret_number = random.randint(min_num, max_num)
        self.attempts = 0

    def play(self):
        print(f"Welcome to Guess the Number Game! I'm thinking of a number between {self.min_num} and {self.max_num}.")
        while True:
            guess = int(input("Take a guess: "))
            self.attempts += 1

            if guess < self.secret_number:
                print("Too low! Try again.")
            elif guess > self.secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {self.secret_number} in {self.attempts} attempts!")
                break

# Example usage:
game = GuessTheNumber(1, 100)
game.play()