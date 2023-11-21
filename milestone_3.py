import random
word_list = ['banana', 'strawberry', 'grape', 'blackberry', 'blackcurrant']

class Hangman():
   
    def __init__(self, word_list):
        self.word_list = word_list

    def generate_random_word(self):
        word = random.choice(word_list)
        return word
    
    def take_user_guess(self):
        guess = str(input("Enter a letter you think may be in the random word: "))

        if len(guess) == 1:
            return guess
        else:
            print("Oops! That is not a valid input.")
            guess = str(input("Enter a letter you think may be in the random word"))

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

    def ask_for_input(self):
        while(True):
            guess = game1.take_user_guess()
            if guess.isalpha() == True:
                break
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")
        self.check_guess(guess)

game1 = Hangman(word_list)
word = game1.generate_random_word()
game1.ask_for_input()


