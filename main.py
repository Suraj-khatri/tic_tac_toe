
import random

board = ['-','-','-',
        '-','-','-',
        '-','-','-',]

current_player='X'
winner = None
game_running = True


# printing the board
def print_board(board):
    print(board[0] + ' | ' + board[1] +' | ' + board[2])
    print("--------")
    print(board[3] + ' | ' + board[4] +' | ' + board[5])
    print("--------")
    print(board[6] + ' | ' + board[7] +' | ' + board[8])

#take user input
def user_input(board):
    user = int(input(f"PLAYER:{current_player}, enter your choice(1-9) :"))
    if user>=1 and user<=9 and board[user-1]=='-':
        board[user-1] = current_player
    else:
        print("OH NO....WRONG INPUT!!!")


#check for win or tie





#check for winner
def check_horizontal(board):
    global winner
    if (board[0] == board[1] == board[2]) and board[1]!='-':
        winner = board[0]
        return True
    elif (board[3] == board[4] == board[5]) and board[5]!='-':
        winner = board[3]
        return True
    elif (board[6] == board[7] == board[8]) and board[8]!='-':
        winner = board[6]
        return True

def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0]!='-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1]!='-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2]!='-':
        winner = board[2]
        return True

def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0]!='-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[1]!='-':
        winner = board[2]
        return True

#check for win or lose
def checkwin():
    if check_horizontal(board) or check_vertical(board) or check_diagonal(board):
        print(f"winner is {winner}")

    
def check_tie(board):
    global game_running
    if "-" not in board:
        print_board(board)
        print("its a tie!!!")
        game_running = False
    


#switch the player
def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

def computer(board):
    #since 1st current_player is 'X' so,
    while current_player == 'O':
        pos = random.randint(0, 8)
        if board[pos] == '-':
            board[pos] = 'O'
            #now we have to call switch_player again
            switch_player()
 

while game_running:
    print_board(board)
    user_input(board)
    checkwin()
    check_tie(board)
    switch_player()

    #now we have to call  computer
    computer(board)
    checkwin()