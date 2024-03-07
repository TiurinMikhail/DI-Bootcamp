# Mini-Project - Tic Tac Toe
print('Welcome to TIC TAC TOE!')


def print_matrix(matrix, n, width=1):
    print('*' * 17)
    for r in range(n):
        for c in range(n):
            if c == 0:
                print('* ', str(matrix[r][c]).ljust(width), end='|')
            if c == 1:
                print(str(matrix[r][c]).ljust(width), end='|')
            elif c == 2:
                print(str(matrix[r][c]).ljust(width), ' *', end='\n')
        if r != 2:
            print('*  ---|---|---  *')
    print('*' * 17)


matrix_tic_tac = [['   '] * 3 for i in range(3)]


def display_board():
    print('TIC TAC TOE')
    print_matrix(matrix_tic_tac, 3, )

def correct_input(row,column):
    if matrix_tic_tac[row][column] == '   ':
        return True
    elif matrix_tic_tac[row][column] != '   ':
        return False

def player_input(player):
    cor_input = False
    while not cor_input:
        row = int(input('Enter row number: '))
        column = int(input('Enter column number: '))
        if correct_input(row,column):
            cor_input = True
        else:
             print('This field already has a value. Try enter again.')
    if player == 'X' and matrix_tic_tac[row][column] == '   ':
        matrix_tic_tac[row][column] = ' X '
    elif player == 'O' and matrix_tic_tac[row][column] == '   ':
        matrix_tic_tac[row][column] = ' O '


def check_win(matrix):
    # Check rows
    for row in matrix:
        if row[0] == row[1] == row[2] == " X " or row[0] == row[1] == row[2] == " O ":
            return True
    # Check columns
    for col in range(3):
        if matrix[0][col] == matrix[1][col] == matrix[2][col] == " X " or matrix[0][col] == matrix[1][col] == matrix[2][col] == " O ":
            return True
    # Check diagonals
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == " X " or matrix[0][0] == matrix[1][1] == matrix[2][2] == " O ":
        return True
    if matrix[0][2] == matrix[1][1] == matrix[2][0] == " X " or matrix[0][2] == matrix[1][1] == matrix[2][0] == " O ":
        return True
    return False


def main():
    winner_name = ''
    cnt = 0
    while not winner_name:
        display_board()
        print("Player X's turn...")
        player_input('X')
        cnt += 1
        display_board()
        if check_win(matrix_tic_tac):
            winner_name = 'X'
            continue
        if cnt >= 9:
            print("Tie!")
            break
        print("Player O's turn...")
        player_input('O')
        cnt += 1
        display_board()
        if check_win(matrix_tic_tac):
            winner_name = 'O'

    if winner_name:
        print(f"Congratulations to player {winner_name}!")

main()

