# @title Hangman Game
import random

word_list = ["banana", "apple", "pear", "kiwi", "orange"]
print(word_list)
word = random.choice(word_list)
print(word)
guess = input()
print(type(guess))
if guess.isalpha() and len(guess) == 1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

    
