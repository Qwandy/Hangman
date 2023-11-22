import random
word_list = ['banana', 'strawberry', 'grape', 'blackberry', 'blackcurrant']

class Hangman():
   
    '''Initialises the Hangman object, takes a list of words as input.'''
    def __init__(self, word_list):
        self.word_list = word_list

    '''Generates a random word and returns it'''
    def generate_random_word(self):
        word = random.choice(word_list)
        return word
    
    '''Asks the user for a letter. Checks that the input is in part of the alphabet and that the length
    of the guess is 1. If these checks do not pass, the user remains in an infinite loop
    which keeps asking them for an input until they input 1 single str character. Calls the check_guess
    method to see if the letter is in the random word and prints if it is.'''
    def ask_for_input(self):

        while(True):
            guess = str(input("Enter a letter you think may be in the random word: "))
            if guess.isalpha() and len(guess) == 1:
                break
            else:
                guess = str(input("Enter a letter you think may be in the random word: "))
        self.check_guess(guess)


    '''Checks if the guessed letter is in the word.'''
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

    

game1 = Hangman(word_list)
word = game1.generate_random_word()
game1.ask_for_input()


