def display_board(board):

    print('   |   |   ')
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print('   |   |   ')

def player_input():

    marker = ' '
    while not (marker == 'X' or marker == 'Y'):
        marker = input('Player 1, do you want X or O? ').upper()

        if marker == 'X':
            return ('X','O')
        else:
            return ('O','X')

def place_marker(board, marker, position):

    # places given player's marker in the selected position on the board
    board[position] = marker

def win_check(board, mark):

    # checks if marks are in a row that results as a win, returns true if they do
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or    # across top
    (board[4] == mark and board[5] == mark and board[6] == mark) or             # across middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or             # across bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or             # down left
    (board[8] == mark and board[5] == mark and board[2] == mark) or             # down middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or             # down right
    (board[7] == mark and board[5] == mark and board[3] == mark) or             # \
    (board[9] == mark and board[5] == mark and board[1] == mark))                # /
        
def choose_first():
    import random

    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):

    return board[position] == ' '

def full_board_check(board):

    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input(f'{turn}, choose your next position (1-9): '))
        
    return position

def replay():
    
    return input('Would you like to play again? (Y/N): ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
    board = [' '] * 10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    
    print(f'{turn} will go first')

    play_game = input('Are you ready to play? (Y/N): ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        # player 1 turn
        if turn == 'Player 1':

            display_board(board)
            position = player_choice(board)
            place_marker(board,player1_marker,position)

            if win_check(board, player1_marker):
                display_board(board)
                print('Congratulations, Player 1! You win!')
                game_on = False
            else:
                turn = 'Player 2'

        # player 2 turn
        else:
            
            display_board(board)
            position = player_choice(board)
            place_marker(board,player2_marker,position)

            if win_check(board, player2_marker):
                display_board(board)
                print('Congratulations, Player 2! You win!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("It's a draw!")
                    break
                else:
                    turn = 'Player 1'
        
    if not replay():
        break