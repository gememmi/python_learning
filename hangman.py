import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase) 
    used_letters = set()  
    
    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0: 
        # letters used
        # ' '.join(['a', 'b', 'c']) --> 'a b c'
        print( 'You have ', lives, 'lives left and you have you have used these letters: ', ''.join(used_letters))
        # what the current word is(ie W - R D)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print('Current word: ', ''.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives -1
        elif user_letter in used_letters:
            print('You have already used that character. Please try again')
        else:
            print("Not a valid character, try a valid character")

    if lives == 0:
        print('Sorry, you died')
    else:
        print('You guessed the word', word, '!')

hangman()


# We first need to make sure that the randome word we are choosing is actually valid, so we create function to test that. 
# We create a while function that will keep finding a random word until it is valid.
# We bring that valid found word into our next funciton by calling that first function. 
# and assiging it to a variable called word. Next we make a set, or object, of letters from the word.
# We create an empty set where we will add all the letters that the user has already guessed
# We create an input field for the user to guess a letter and make it uppercase
# Then we create a condition so that if the users guess is valid and not in the used letttesr
# then add that letter to the used letters. Then if that guess in the actual word, remove that letter from the 
# word. If the users guess is in the used letters, send them a message. If the users guess is not in the used letters
# and not in the alphabet, print a message that their guess is not valid. 
# We want the use to be able to see what letters they have already guess so we can join the used_letters together using .join() which we use on an empty string. 
# Then we create a list that will contain the letter 