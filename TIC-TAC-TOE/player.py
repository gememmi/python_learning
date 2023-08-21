import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

        # we want all players to get their next move

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
    #   get a random valid spot for our next move
      square = random.choice(game.available_moves)
      return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    # def __repr__(self):
    #     return "Letter: {}".format(self.letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
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


