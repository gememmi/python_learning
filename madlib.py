# STRING CONCATENATION (aka how to put strings together)
# suppose we want to create a string that says "subscribe to __
# youtuber = "Emily Daniels"
# some string variable


# a few ways to do this

# print( 'subscribe to ' + youtuber)
# print('subscribe to {}'.format(youtuber))
# print(f'subscribe to {youtuber}')

# this last one is the cleanest way to concatenate

adj = input("Adjective: ")
verb = input("Verb: ")
verb2= input("Verb: ")
famous_person = input("Famous person: ")
madlib = f"Computer Programming is so {adj}! It makes me so excited all the time because \
I love to {verb}. Stay hydrated and {verb2} like you are {famous_person}!"
print(madlib)

# WHAT I LEARNED:
# -input() allows an input field when you run the program, it will run one input at a time. You can than use the variable input and print this information.
# -you can use the \ forward slash to indicate a string that continues to the next line, in Python./
# -The simplest way to concatentate is to use an F string meaning: f""
