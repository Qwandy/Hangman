import random
word_list = ['banana', 'strawberry', 'grape', 'blackberry', 'blackcurrant']

class Hangman():
   
    def __init__(self, word_list):
        self.word_list = word_list

    def generate_random_word(self):
        word = random.choice(word_list)
        return word
    
    def take_user_guess(self):
        guess = str(input("Enter a letter you think may be in the random word"))

        if len(guess) == 1:
            print("Good guess!")
            return guess
        else:
            print("Oops! That is not a valid input.")
            guess = str(input("Enter a letter you think may be in the random word"))

game_1 = Hangman(word_list)
secret_word = game_1.generate_random_word()
first_guess = game_1.take_user_guess()


