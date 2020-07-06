def is_valid_move(board, row, column, direction):
    condition1 = board[row - 1][column - 1] == '@'
    if direction == 1:
        if row <= 2:
            condition2, condition3 = False, False
        else:
            condition2 = board[row - 2][column - 1] == '@'
            condition3 = board[row - 3][column - 1] == '-'
    elif direction == 2:
        if row >= len(board) - 1:
            condition2, condition3 = False, False
        else:
            condition2 = board[row][column - 1] == '@'
            condition3 = board[row + 1][column - 1] == '-'

    elif direction == 3:
        if column <= 2:
            condition2, condition3 = False, False
        else:
            condition2 = board[row - 1][column - 2] == '@'
            condition3 = board[row - 1][column - 3] == '-'

    elif direction == 4:
        if column >= len(board[0]) - 1:
            condition2, condition3 = False, False
        else:
            condition2 = board[row - 1][column] == '@'
            condition3 = board[row - 1][column + 1] == '-'
    else:
        return False

    if condition1 and condition2 and condition3:
        return True
    else:
        return False


def perform_move(board, row, column, direction):
    if is_valid_move(board, row, column, direction):
        board[row - 1][column - 1] = '-'
        if direction == 1:
            board[row - 2][column - 1] = '-'
            board[row - 3][column - 1] = '@'
        elif direction == 2:
            board[row][column - 1] == '-'
            board[row + 1][column - 1] = '@'
        elif direction == 3:
            board[row - 1][column - 2] = '-'
            board[row - 1][column - 3] = '@'
        elif direction == 4:
            board[row - 1][column] = '-'
            board[row - 1][column + 1] = '@'
        else:
            return board
    else:
        return board
    return board


def count_pegs_remaining(board):
    cnt = 0
    for i in board:
        for j in i:
            if j == '@':
                cnt += 1
    return cnt


def count_moves_available(board):
    cnt = 0
    for i in range(1, len(board) + 1):
        for j in range(1, len(board[0]) + 1):
            for k in range(1, 5):
                if is_valid_move(board, i, j, k):
                    cnt += 1
    return cnt


def read_valid_move(board):
    column = read_valid_int(
        "Choose the COLUMN of a peg you'd like to move: ", 1, len(board[0]))
    row = read_valid_int(
        "Choose the ROW of a peg you'd like to move: ", 1, len(board))
    direction = read_valid_int(
        "Choose a DIRECTION to move that peg 1) UP, 2) DOWN, 3) LEFT, or 4) RIGHT: ", 1, 4)
    if is_valid_move(board, row, column, direction):
        return column, row, direction
    else:
        directionString = 'UP' if direction == 1 else 'DOWN' if direction == 2 else 'LEFT' if direction == 3 else 'RIGHT'
        print('Moving a peg from row {} and column {} {} is not currently a legal move.\n'.format(
            row, column, directionString))
        return read_valid_move(board)


def display_board(board):
    print('\n  ', end='')
    for i in range(1, len(board[0])+1):
        print(i, end=' ')
    print()
    for i in range(len(board)):
        print(i+1, end=' ')
        for j in board[i]:
            print(j, end=' ')
        print()


def create_board(board_type):
    if board_type == 1:
        return [
            ["#", "#", "#", "@", "@", "@", "#", "#", "#"],
            ["#", "#", "#", "@", "@", "@", "#", "#", "#"],
            ["@", "@", "@", "@", "@", "@", "@", "@", "@"],
            ["@", "@", "@", "@", "-", "@", "@", "@", "@"],
            ["@", "@", "@", "@", "@", "@", "@", "@", "@"],
            ["#", "#", "#", "@", "@", "@", "#", "#", "#"],
            ["#", "#", "#", "@", "@", "@", "#", "#", "#"],
        ]
    elif board_type == 2:
        return [
            ["#", "-", "@", "@", "-", "#"],
            ["-", "@", "@", "@", "@", "-"],
            ["@", "@", "@", "@", "@", "@"],
            ["@", "@", "@", "@", "@", "@"],
            ["-", "@", "@", "@", "@", "-"],
            ["#", "-", "@", "@", "-", "#"],
        ]

    elif board_type == 3:
        return [['#', '#', '#', '-', '@', '-', '#', '#', '#'],
                ['#', '#', '-', '@', '@', '@', '-', '#', '#'],
                ['#', '-', '@', '@', '-', '@', '@', '-', '#'],
                ['-', '@', '@', '@', '@', '@', '@', '@', '-']]
    elif board_type == 4:
        return [['-', '-', '-', '-', '-'],
                ['-', '@', '@', '@', '-'],
                ['-', '-', '@', '-', '-'],
                ['-', '-', '@', '-', '-'],
                ['-', '-', '-', '-', '-']]
    else:
        return None


def read_valid_int(prompt, minval, maxval):
    userinput = input(prompt)
    if userinput.isdigit():
        integer = int(userinput)
        if integer < minval or integer > maxval:
            return read_valid_int(
                "Please enter your choice as an integer between {} and {}: ".format(
                    minval, maxval),
                minval,
                maxval,
            )
        else:
            return integer
    else:
        return read_valid_int(
            "Please enter your choice as an integer between {} and {}: ".format(
                minval, maxval), minval, maxval
        )


def main():
    print("\nWELCOME TO CS300 PEG SOLITAIRE!")
    print("===============================\n")
    print(
        """Board Style Menu
	1) Cross
	2) Circle
	3) Triangle
	4) Simple T"""
    )
    board_type = read_valid_int("Choose a board style: ", 1, 4)
    board = create_board(board_type)
    while True:
        display_board(board)
        if count_pegs_remaining(board) == 1:
            print('Congrats, you won!')
            break
        elif count_moves_available(board) == 0:
            print('It looks like there are no more legal moves.  Please try again.')
            break
        else:
            pass
        column, row, direction = read_valid_move(board)
        board = perform_move(board, row, column, direction)
    print('\n==========================================')
    print('THANK YOU FOR PLAYING CS300 PEG SOLITAIRE!')


main()
