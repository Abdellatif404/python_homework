

board = [' ']*9


def tic_tac_toe():
    print('Welcome to Tic Tac Toe!')
    player = 'first'
    symbol = input('Player 1: select your symbol X or O:\t')

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
        if check_win(positions[0], positions[1], positions[2]):
            return False

    return True


def check_win(p1, p2, p3):
    
    if board[p1] == board[p2] == board[p3] == 'X' or board[p1] == board[p2] == board[p3] == 'O':
        return True
    return False


def print_board():
    print(f'{board[6]} | {board[7]} | {board[8]}'
          f'\n{board[3]} | {board[4]} | {board[5]}'
          f'\n{board[0]} | {board[1]} | {board[2]}')


def reset_info(variable, old_value, new_value):
    if variable == old_value:
        variable = new_value
    else:
        variable = old_value
    return variable


tic_tac_toe()
