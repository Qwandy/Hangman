import random

word_list = ['banana', 'strawberry', 'grape', 'blackberry', 'blackcurrant']

word = random.choice(word_list)


guess = str(input("Enter a letter you think may be in the random word"))

if len(guess) == 1:
    print("Thank you for your guess")
else:
    print("Your guess is not valid, guess again but make sure it is one character")