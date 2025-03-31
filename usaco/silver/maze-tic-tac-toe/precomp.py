import itertools
import pprint

def is_winning(board):
    winning_lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]
    for a, b, c in winning_lines:
        if board[a] == 'm' and board[b] == 'o' and board[c] == 'o':
            return True
        if board[a] == 'o' and board[b] == 'o' and board[c] == 'm':
            return True
    return False

def board_to_2d_list(board):
    return [list(board[i:i+3]) for i in range(0, 9, 3)]

def get():
    cells = ['m', 'o', ' ']
    winning_boards = []
    for board in itertools.product(cells, repeat=9):
        if is_winning(board):
            winning_boards.append(board_to_2d_list(board))
    return winning_boards


