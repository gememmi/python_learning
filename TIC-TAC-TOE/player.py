import math
import random


class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

        # we want all players to get their next move
        # place holder method that ensures all subclasses have this method, pass overrides it
    def get_move(self, game):
        pass

# subclass of Player class
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
    #   get a random valid spot for our next move
      square = random.choice(game.available_moves())
      return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    # def __repr__(self):
    #     return "Letter: {}".format(self.letter)

    # gets user input for a move and validates whether the input is a valid move, ie an available move
   
    # game refers to a instance of a tic tac toe game
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # here we try to conver the user input to an integer, if not an integer than the program raises an error
            # we hand exceptions in the while until we get a valid input
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again')

        return val


# UNDERSTANDING CLASSES:
# Each variable assiged creates an object, OOP, for example a list belongs to the List class
# call type() on an object to find out what class your object belongs to 
# call dir() on an object to find out what methods are allowed to be used on the class. 
# __init__ is the initializer method. It initializes the attributes of the object. It is automatically called whenteh object is created. Think back to what we learned in Ruby!!
# So we are creating a HumanPlayer and a ComputerPlayer object that each have their own attibutes. 
# pass indicates that nothing is defined. 
# Object in relation to classes is the same thing as an INSTANCE. 

# DEF INIT: So when we are use the initializer method under a class, we are initializing the attributes of that class. This method takes in different arguments, self and letter. SELF refers to the object, which will be created later. You can also use it to acces the attributes of that class. The following arguments are used to store the specific attribute's value of the object. So self.attribute are the defined attributes and the arguments of the same name is used to store the value of the attribute. 

# DEF REPR: allows us to print attribute information in a more sophisticated way. Takes in the argument self. Add this method under a class to format the return of the attributes. 

# INSTANCE METHODS: take an input parameter of self to access the attributes fo the class. get_move is an example of an instance method. 

# BASE CLASSES, WHY?:
# establish common interface and behavior that all Player subclasses should follow. This helps you avoid duplicating code for shared functionalities.
# Subclasses are basically specialized cases of the base class. So the base class allows the subclasses to inherit properties and behaviors and then add their own distinct characteristics. Both of our subclasses inherit the concept of making moves, but the implement them differently.
# Computer makes a random choice move and HumanPlayer.
# SUPER FUNCTION: is used to call methods from the parent class within the subclass. It ensures that the behavior defined in the parents clas is still executed while allowing the subclass to add its own unique functionality. This is espeically important when you wnat to extend the functionality ofthe parent class rath then completely replacing it. 
# So in our subclasses the "letter" attribute is properly initialized through the base class using super().__init__(letter)