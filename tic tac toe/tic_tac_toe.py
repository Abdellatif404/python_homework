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
    print('Welcome to Tic Tac Toe!')
    player = 'first'
    symbol = input('Player1: select your symbol (X or O):\t')

    while symbol.upper() not in 'XO':
        print('Please choose X or O')
        symbol = input('Try again:\t')

    while game_on():
        position = input(f'{player} player select your position (1-9):\t')

        if position.isdigit() and 0 < int(position) < 10:

            if board[int(position) - 1] == ' ':
                board[int(position) - 1] = symbol.upper()
                print_board()

                if not game_on():
                    print(f'CONGRATULATIONS: The {player} player WON')

                symbol = reset_info(symbol.upper(), 'X', 'O')
                player = reset_info(player, 'second', 'first')


def game_on():
    winner_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for positions in winner_positions:
        if check_win(positions):
            return False

    return True


def check_win(ls):
    x_win = 0
    o_win = 0

    for position in ls:
        if board[position] == 'X':
            x_win += 1
        elif board[position] == 'O':
            o_win += 1

    return x_win == 3 or o_win == 3


def print_board():
    print(f'{board[6]} | {board[7]} | {board[8]}'
          f'\n{board[3]} | {board[4]} | {board[5]}'
          f'\n{board[0]} | {board[1]} | {board[2]}')


def reset_info(info, old, instead):
    if info == old:
        info = instead
    else:
        info = old
    return info


tic_tac_toe()
