import random
from words import words
import string


def get_valid_word(words):
    # random.choice allows you to choose a random thing from a list
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
        # so if a word contains a space or a dash, we will keep iterating until we find one without.

    return word.upper()

def hangman():
    word = get_valid_word(words)
    # we use the valid word that our first function found for us and then use it in this funcion
    word_letters = set(word) 
    # set creates an object so here we are creating an object of single letter singles from our chosen word
    alphabet = set(string.ascii_uppercase)
    # what the user has already guess will get moved here
    used_letters = set()   
    # users letter guess in uppercase
    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print('You have already used that character. Please try again')
    else:
        user_letter in alphabet
        print("Not a valid character, try a valid character")

user_input = input("Type something: ")
print(user_input)