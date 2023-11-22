# Hangman Project

This is the documentation page for my hangman project.

This game lets you play Hangman in Python. There are a total of 5 words you can guess! Even though the project is complete I may incorporate a database of words in the future so that the game is more challenging. The aim of this project was to create a functional version of Hangman using text and get some practice using OOP in Python while doing so. An additional aim was to get more practice using Version control while working on a project. I have achieved these aims and feel more confident in using Python classes and Git.

## Installation: 
None. Just run milestone_4.py, it uses no third party python packages, just random which is inbuilt to Python.


## Features:
- Hangman class which contains all of the methods associated with the game hangman.
- 'generate_random_word' method which sets self.word to a random word, sets word_guessed to a list of underscores representing a group of characters that are to be guessed in the game, and sets the number of letters to be guessed as an additional attribute.
- 'take_user_input' method which asks for a single letter user input. This is the method which runs the game as it puts the user in an infinite loop (which can be broken by typing 'esc') and repeatedly asks the user to input guesses. It makes sure that the input is a single alphabetical character and keeps track of a list of already tried guesses. Since it runs the core of the game, it will break the loop if the user is out of lives.
- 'check_guess' method which checks if the user guess is in the random word and prints if it is or is not. It also replaces underscores in the word_guessed attribute with the correct guess at the correct indexes. It also tells the user how many letters they still need to guess.
- You can control the difficulty of the game by setting 'num_lives' to a value of your choosing when calling the Hangman class. By default it is set to 5.
- You can win or lose by either guessing all the characters in the word while having more than 1 life left or running out of lives.

## File structure:
Each successive milestone is a less skeletal version of the final project. It is recommended you play with milestone_4.py otherwise there are a lot of unincorporatd features. It's uploaded in this format as this is an AiCore project.

## License:
 No license. This project is free to use for any purposes. Most likely you will just play the game though.



