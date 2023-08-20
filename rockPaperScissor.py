import random

def play():
    user = str(input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors \n" ))
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "tie"
    
    if is_win(user, computer):
        return 'You win!'
    
    return 'You lost'


# r > s, s > p, p > r

def is_win(player, opponent):
    # return true if the player wine
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
        
print(play())