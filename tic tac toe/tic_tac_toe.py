# Your assignment: Create a Tic Tac Toe game. You are free to use any IDE you like.
#
# Here are the requirements:
#
# 2 players should be able to play the game (both sitting at the same computer)
# 1\ The board should be printed out every time a player makes a move
# 2\ You should be able to accept input of the player position and then place a symbol on the board
# Feel free to use Google to help you figure anything out (but don't just Google "Tic Tac Toe in
# Python" otherwise you won't learn anything!) Keep in mind that this project can take anywhere
# between several hours to several days.
#
# HAVE FUN!

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def tic_tac_toe():
    player = 'first'
    symbol = input('first player select your symbol (X or O):\t')

    while symbol.upper() not in 'XO':
        print('Please choose X or O')
        symbol = input('Try again:\t')

    while game_state():
        selected_number = input(f'{player} player select a number (1-9):\t')

        if selected_number.isdigit() and 0 < int(selected_number) < 10:
            if board[int(selected_number) - 1] == ' ':
                board[int(selected_number) - 1] = symbol.upper()

                print_board()

                if not game_state():
                    print(f'CONGRATULATIONS: The {player} player WON')

                if symbol.upper() == 'X':
                    symbol = 'O'
                else:
                    symbol = 'X'
                if player == 'first':
                    player = 'second'
                else:
                    player = 'first'


def game_state():
    game_on = True
    win_indexes = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win_list in win_indexes:
        if check_rows(win_list):
            game_on = False

    return game_on


def check_rows(ls):
    if board[ls[0]] == board[ls[1]] == board[ls[2]] == 'X' or board[ls[0]] == board[ls[1]] == board[ls[2]] == 'O':
        return True
    return False


def print_board():
    print(f'{board[6]} | {board[7]} | {board[8]}'
          f'\n{board[3]} | {board[4]} | {board[5]}'
          f'\n{board[0]} | {board[1]} | {board[2]}')


tic_tac_toe()
