import os

def draw(board):
    for i in range(0, 9, 3):
        print(' ' + board[i] + '|' + board[i + 1] + '|' + board[i + 2] + '|')

def take_input(board, spaces, turn):
    pos = -1
    print(turn + "'s turn")
    while pos == -1:
        try:
            print("enter the position from 1 to 9")
            pos = int(input())
            if pos < 1 or pos > 9:
                pos = -1
            elif board[pos - 1] != ' ':
                pos = -1
        except ValueError:
            print("enter a valid position")

    index = pos - 1
    board[index] = turn
    spaces -= 1
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

    return board, spaces, turn  # Return the updated values

def check_win(board):
    for i in range(0, 9, 3):
        if board[i] != ' ' and board[i] == board[i + 1] == board[i + 2]:
            return board[i]

    for i in range(3):
        if board[i] != ' ' and board[i] == board[i + 3] == board[i + 6]:
            return board[i]

    if board[0] != ' ' and board[0] == board[4] == board[8]:
        return board[0]

    if board[2] != ' ' and board[2] == board[4] == board[6]:
        return board[2]

    return 0


def tic_tac_toe():
    spaces = 9
    turn = 'X'
    board = [' '] * 9
    win = False

    while not win and spaces >= 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        draw(board)
        board, spaces, turn = take_input(board, spaces, turn)
        win = check_win(board)

    os.system('cls' if os.name == 'nt' else 'clear')
    draw(board)
    if win:
        print(f"{win} wins")
    else:
        print("It's a draw")

tic_tac_toe()