from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer

# class for a game instace
class TicTacToe:
    # initializes each game with a game board of 9 squares and a variable to track the current winner
    def __init__(self):
        # generates a list with 9 elements, each elemetn being a space
        self.board =  [' ' for _ in range(9)] # we will use single list of rep 3x3
        self.current_winner = None # keep track of winner!

#   this funciton prints the state of the board in a user friendly format
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    #  return  ['x', 'x', 'o'] --> [(0,'x'), (1, 'x'),(2, 'o')]
    
    def empty_squares(self):
        return ' ' in self.board
    # returns any empty spaces in the board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    # this just returns the number of empty squares in the board
    
    def make_move(self, square, letter):
        # if valid move, then make the move (assigne square to letter)
        # then retrun true. if invalid, retunr false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # check the row
        row_ind = square // 3 
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all(spot == letter for spot in row):
            return True
        
        # check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
    
        # check diagonal, check if even number
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()
    
    letter = 'X' # starting letter
    # iterate while the game still has empty squares
    while game.empty_squares():
        # so while it is still true that there are empty squares
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print(' ')
            
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'

    if print_game:
                print('It\s a tie!')
if __name__ == '__main__':
    x_player = HumanPlayer('X') 
    o_player = GeniusComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)             



    # When we first create the game instance with a a board we use: self.board =  [' ' for _ in range(9)]. But what does this mean? We are initalizing a list of 9 empty spaces by running a for loop with a - variable 9 times. So we are saying making a space for each element in a range of 9.

    # EXPLAIN HOW WE SET UP THE BOARD: for each instance of the game, we are taking the list of 9 spaces that we created earlier. The first index,0, will be used to split the board into the first 3 indexes. This will only be done for the first 3 indexes.
    # So we are creating 3 rows fo 3 elements. For each row, we are printing the lines.

    # @staticmethod? this means that the function belongs to the class itself, not the instance of the class. it can be called on the class itself, without creating an instace of the class.
    # does not take a self parameter. We are using this method to print the numbers on the board in order to inform the player how to access each space. 
    # Does not require access to instacne-specific data. 

    # How do we print the numbers? print_board_numbers funtion created varible number_board which is comprised of
    # the variable is a list that will loop over the first 3 elements, current index is turned into a string and then joined with the bars to create the
    # board format. 

    # WHAT IS LIST COMPREHESION: takes the place of a for loop. 

    # The available_moves function returns only the indices representing the empty spots on the game board
    # it does this by iterating over the board, giving each spot an numbered index and then only returning the spots that have an empty space. 
    # It returns a list of tuples of the available moves with their indexes. We then reference this function in our player.py file.  