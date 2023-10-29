# @title Hangman Game
import random

word_list = ["banana", "apple", "pear", "kiwi", "orange"]
print(word_list)
word = random.choice(word_list)
print(word)
word_guessed = [*word]
display_guessed_word = [*word]
for letter in range(len(display_guessed_word)):
    display_guessed_word[letter] = "_"
print(display_guessed_word)
num_letters = len(list(dict.fromkeys(word_guessed)))
print(num_letters)
num_lives = int(5)
list_of_guesses = []



def check_guess(guess):
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
        for letter in range(len(word_guessed)):
            if guess == word_guessed[letter]:
                display_guessed_word[letter] = guess
        global num_letters
        num_letters -= 1
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        global num_lives
        num_lives -= 1
        print(f"You have {num_lives} lives left.")

def ask_for_input():
    guess = input()
    print(type(guess))
    if guess.isalpha() == False or len(guess) != 1:
        print("Invalid letter. Please enter a single alphabetical character.")
    elif guess in list_of_guesses:
        print("You already tried that letter")   
        print(list_of_guesses)         
    else:
        guess = guess.lower()
        check_guess(guess)
        list_of_guesses.append(guess)
        print(list_of_guesses)
        print(display_guessed_word)

def play_game(word_list):
    #game = hangman(word_list, num_lives)
    print("Lets play Hangman! Please enter a single letter below.")
    play_hangman = True
    while play_hangman == True:
        if num_lives == 0:
            print("You lost!")
            play_hangman = False
            return
        elif num_letters > 0:
            ask_for_input()
        else:
            print("Congratualtions. You won the game!")
            return

play_game(word_list)
