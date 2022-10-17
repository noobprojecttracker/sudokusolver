import random
import time

incomplete = [['4', '3', 'x', '2', '6', '9', 'x', 'x', '1'], ['6', 'x', '2', 'x', 'x', '1', 'x', '9', '3'],
              ['1', 'x', '7', 'x', 'x', '4', '5', '6', '2'], ['8', 'x', '6', '1', '9', '5', 'x', 'x', '7'],
              ['x', 'x', '4', '6', '8', 'x', '9', '1', '5'], ['9', 'x', '1', '7', '4', '3', '6', 'x', 'x'],
              ['5', 'x', '9', 'x', '2', 'x', 'x', '7', '4'], ['2', '4', 'x', '9', '5', '7', 'x', '3', '6'],
              ['x', '6', '3', '4', '1', '8', 'x', 'x', '9']]

valid = [['4', '3', '5', '2', '6', '9', '7', '8', '1'], ['6', '8', '2', '5', '7', '1', '4', '9', '3'],
         ['1', '9', '7', '8', '3', '4', '5', '6', '2'], ['8', '2', '6', '1', '9', '5', '3', '4', '7'],
         ['3', '7', '4', '6', '8', '2', '9', '1', '5'], ['9', '5', '1', '7', '4', '3', '6', '2', '8'],
         ['5', '1', '9', '3', '2', '6', '8', '7', '4'], ['2', '4', '8', '9', '5', '7', '1', '3', '6'],
         ['7', '6', '3', '4', '1', '8', '2', '5', '9']]

invalid = [['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
           ['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
           ['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
           ['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
           ['1', '2', '3', '4', '5', '6', '7', '8', '9'], ]

one_off = [['x', '3', '5', '2', '6', '9', '7', '8', '1'], ['6', '8', '2', '5', '7', '1', '4', '9', '3'],
           ['1', '9', '7', '8', '3', '4', '5', '6', '2'], ['8', '2', '6', '1', '9', '5', '3', '4', '7'],
           ['3', '7', '4', '6', '8', '2', '9', '1', '5'], ['9', '5', '1', '7', '4', '3', '6', '2', '8'],
           ['5', '1', '9', '3', '2', '6', '8', '7', '4'], ['2', '4', '8', '9', '5', '7', '1', '3', '6'],
           ['7', '6', '3', '4', '1', '8', '2', '5', '9']]

hardest = [['x', 'x', '6', '4', '3', 'x', 'x', 'x', '1'], ['x', 'x', 'x', 'x', 'x', '6', 'x', 'x', 'x'],
           ['4', 'x', 'x', 'x', 'x', '1', '2', '5', 'x'], ['x', '6', 'x', '1', 'x', 'x', 'x', 'x', 'x'],
           ['x', 'x', 'x', '8', 'x', '7', 'x', 'x', '5'], ['1', '9', 'x', 'x', '2', 'x', 'x', 'x', 'x'],
           ['x', 'x', '5', '7', 'x', 'x', 'x', '3', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', '9', 'x'],
           ['2', 'x', 'x', 'x', 'x', 'x', '7', 'x', 'x']]


def print_board(board):
    for row in board:
        print('  '.join(row))


def valid_rows(board):
    s = 0

    for row in board:
        if row.count('1') <= 1 and row.count('2') <= 1 and row.count('3') <= 1 and row.count('4') <= 1 and row.count(
                '5') <= 1 and row.count('6') <= 1 and row.count('7') <= 1 and row.count('8') <= 1 and row.count(
                '9') <= 1:
            s += 1

    if s == 9:
        # print('valid rows')
        return True


def valid_columns(board):
    s = 0

    for col in range(9):
        column = board[0][col] + board[1][col] + board[2][col] + board[3][col] + board[4][col] + board[5][col] + \
                 board[6][col] + board[7][col] + board[8][col]
        if column.count('1') <= 1 and column.count('2') <= 1 and column.count('3') <= 1 and column.count(
                '4') <= 1 and column.count('5') <= 1 and column.count('6') <= 1 and column.count(
                '7') <= 1 and column.count('8') <= 1 and column.count('9') <= 1:
            s += 1

    if s == 9:
        # print('valid columns')
        return True


def valid_three_by_threes(board):
    s = 0

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):

            b = list(board[row][col] + board[row][col + 1] + board[row][col + 2] + board[row + 1][col] + board[row + 1][
                col + 1] + board[row + 1][col + 2] + board[row + 2][col] + board[row + 2][col + 1] + board[row + 2][
                         col + 2])

            # test if valid...
            if b.count('1') <= 1 and b.count('2') <= 1 and b.count('3') <= 1 and b.count('4') <= 1 and b.count(
                    '5') <= 1 and b.count('6') <= 1 and b.count('7') <= 1 and b.count('8') <= 1 and b.count('9') <= 1:
                s += 1

    if s == 9:
        # print('valid three by threes')
        return True


def valid_board(board):
    if (valid_rows(board)) and (valid_columns(board)) and (valid_three_by_threes(board)):
        # print('This board is valid.')
        return True


def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 'x':
                return (row, col)
    return None


def is_valid(board, value, position):
    for row in range(9):
        if board[position[0]][row] == value and position[1] != row:
            return False

    for row in range(9):
        if board[row][position[1]] == value and position[0] != row:
            return False

    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == value and (i, j) != position:
                return False

    return True


def solve(board):
    find = find_empty(board)

    if not find_empty(board):
        return board

    row, col = find
    candidates = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for value in candidates:
        if is_valid(board, value, (row, col)):
            board[row][col] = value
            if solve(board):
                return board
            board[row][col] = 'x'


def main():

    wants = input('Do you want to solve a sudoku, or generate a sudoku? \n a) solve \n b) generate: ')
    if wants == 'a':
        print('\n')
        board = []
        row = 1
        while len(board) < 9:

            l = []

            new_row = input(f'Please input all values for row number {row}. Unknown values should be inputted as a '
                            f'lowercase x: ')

            while len(new_row) != 9:
                new_row = input(
                    f'Please make sure your row has 9 values! Please input all values for row number {row}. Unknown values should be inputted as a lowercase x: ')

            for char in new_row:
                l.append(char)
            board.append(l)
            l = []
            row += 1

        print('\n')

        print('This is your starting board.')
        print('\n')
        print_board(board)
        print('\n')
        print('Now solving...')
        print('\n')
        t1 = time.time()
        solve(board)
        t2 = time.time()
        if valid_board(board):
            print('This is your new board.')
            print('\n')
            print_board(board)
            print('\n')
            print(f'I solved it in just {t2 - t1} seconds!')
        else:
            print('Board is unsolvable')

    else:

        print('Ok. Generating a valid sudoku now!')

        b = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
             ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
             ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
             ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
             ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ]

        generated = generate_board(b)

        print_board(generated)

        print('\n')
        test = input('Do you want to test your solution? \n a) yes \n b) no: ')

        if test == 'a':
            print('\n')
            print('Ok, here is the solution!')
            print('\n')
            x = solve(generated)
            print_board(x)
        else:
            print('\n')
            print('Ok!')


def generate_board(board):

    x = 0
    candidates = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    choices = [2, 3, 4]
    while x < 9:
        y = random.choice(candidates)
        board[x][random.randrange(1, 9)] = y
        candidates.remove(y)
        x += 1

    if solve(board):

        for row in range(len(board)):
            i = random.choice(choices)
            lol = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            while i > 0:
                m = random.choice(lol)
                board[row][m] = 'x'
                lol.remove(m)
                i -= 1

    return board


if __name__ == "__main__":
    main()


# easy board
# x5xx9xx8x
# 37xxxxx2x
# 1xxxx6x9x
# x4526x8x7
# x6x8xx9x5
# x1x3xx2x6
# 53xxx816x
# xx14xxx7x
# x9xxx3xxx

# hard board
# xxxxxx86x
# xxx8x7xxx
# 8xxx361x2
# 7xxxxxx93
# xx5xxx4xx
# 18xxxxxx6
# 6x819xxx7
# xxx2x3xxx
# x34xxxxxx