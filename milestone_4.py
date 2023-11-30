import random
word_list = ['banana', 'strawberry', 'grape', 'blackberry', 'blackcurrant']

class Hangman():

    
    def __init__(self, word_list, word = None, num_letters = None, word_guessed = None, 
                 list_of_guesses = [], num_lives = 5):
        '''Initialises the Hangman object, takes a list of words as input.'''
        self.word = word
        self.word_list = word_list
        self.word_guessed = word_guessed
        self.num_letters = num_letters
        self.num_lives = num_lives
        self.list_of_guesses = list_of_guesses

    
    def generate_random_word(self):
        '''Generates a random word and returns it'''
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for x in self.word]
        self.num_letters = len(self.word)
        return self.word
    
    
    def ask_for_input(self):
        '''Asks the user for a letter. Checks that the input is in part of the alphabet and that the length
            of the guess is 1. If these checks do not pass, the user remains in an infinite loop
            which keeps asking them for an input until they input 1 single str character. Calls the check_guess
            method to see if the letter is in the random word and prints if it is. If you want to break
            out of the loop before you finish playing, type esc when you make a guess.'''
        while(True):
            guess = str(input("Enter a letter you think may be in the random word: "))

            if guess == "esc": #used to break out of the loop automatically
                break

            if guess.isalpha() and len(guess) != 1: # checks that guess is alphabetical and single digit
                print("Invalid letter. Please, enter a single alphabetical character.")
                guess = str(input("Enter a letter you think may be in the random word: "))
            elif guess in self.list_of_guesses: # Handles response if repeated a guess
                print("You already tried that letter!")
            else: # else statement checks the guess and handles user running out of lives.
                self._check_guess(guess)
                if self.num_lives == 0:
                    print("You have lost!")
                    break
                elif self.num_letters == 0 and self.num_lives >= 1:
                    print("Congratulations, you have won!")
                    break

        #.check_guess(guess)


    
    def _check_guess(self, guess):
        '''Internal method that checks if the guessed letter is in the word.'''
        guess = guess.lower() # makes guess lowercase for functionality reasons
        if guess in self.word: # checks if guess is in the word
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)): # loop replaces underscores with guess at correct idxs
                if guess == self.word[i]:
                    self.word_guessed[i] = guess
                    print(self.word_guessed)
            u_counter = 0 # counter keeps track of number of letters guessed
            for i in self.word_guessed: # loop used to count how many letters guessed
                if i != '_':
                    u_counter += 1
            self.num_letters = len(self.word_guessed) - u_counter # updates num_letters
            print(f"You have {self.num_letters} letters left to guess")
        else: # else statement handles what to do if guess is not in the letter
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left. ")

                

def play_game(word_list):
    '''Internal method that checks if the guessed letter is in the word.'''
    game1 = Hangman(word_list)
    game1.generate_random_word()
    game1.ask_for_input()

play_game(word_list)