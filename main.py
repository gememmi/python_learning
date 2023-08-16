import random
# random is a built-in module of Python that is used to generate random number. Importing this module gives us access to the functions in the random module

def guess(x):
    random_number = random.randint(1,x)
    # our variable random_number will be a random number between 1 and x, x is what ever parameter we pass when we run the program
    guess = 0
    # we want to run the program until the random number is guess, which means we will need a loop with a condition: a WHILE LOOP
    # we have to start our variable somewhere, but we dont want it accidentally be the random number so we start at 0 since our randint must be more than 1 accourding to our parameters
    # while guess != random_number:
    #     guess = int(input(f"Guess a number between 1 and {x}: "))
    #     if guess < random_number:
    #         print("Sorry, guess again. Too low")
    #     elif guess > random_number:
    #         print("Sorry, guess again. Too high")
    # print(f"Yay, congrats you have guessed the number {random_number} correctly")
# guess(10)

def computer_guess(x):
    # we have to set a low and a high bound
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high :
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?')
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess +1

    print(f"YAY, the computer guessed your number, {guess} correctly!!")
computer_guess(10)
