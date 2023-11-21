import random

word_list = ['banana', 'strawberry', 'grape', 'blackberry', 'blackcurrant']


for i in range(5):
    word = random.choice(word_list)
    print(word)
    
print(word_list)