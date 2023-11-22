# Hangman Project

This is the documentation page for my hangman project.

Features:
- Hangman class which contains all of the methods associated with the game hangman.
- 'generate_random_word' method which sets self.word to a random word, sets word_guessed to a list of underscores representing a group of characters that are to be guessed in the game, and sets the number of letters to be guessed as an additional attribute.
- 'take_user_input' method which asks for a single letter user input. This is the method which runs the game as it puts the user in an infinite loop (which can be broken by typing 'esc') and repeatedly asks the user to input guesses. It makes sure that the input is a single alphabetical character and keeps track of a list of already tried guesses. Since it runs the core of the game, it will break the loop if the user is out of lives.
- 'check_guess' method which checks if the user guess is in the random word and prints if it is or is not. It also replaces underscores in the word_guessed attribute with the correct guess at the correct indexes. It also tells the user how many letters they still need to guess.


