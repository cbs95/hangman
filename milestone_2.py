# @title Hangman Game
import random

word_list = ["banana", "apple", "pear", "kiwi", "orange"]
print(word_list)
word = random.choice(word_list)
print(word)


def check_guess(guess):
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    play_hangman = True
    while play_hangman == True:
        guess = input()
        print(type(guess))
        if guess.isalpha() and len(guess) == 1:
            #print("Good guess!")
            play_hangman = False
            guess = guess.lower()
            #return guess
        else:
            print("Oops! That is not a valid input.")
    check_guess(guess)

ask_for_input()
