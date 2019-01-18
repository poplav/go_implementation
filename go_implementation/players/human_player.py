from go_implementation.base_implementation.go_sets import N, flatten
import textwrap


class HumanPlayer:

    def __init__(self, color):
        self.color = color
        self.ko = None

    def get_move(self, board):
        board = textwrap.wrap(board, N)
        for i in range(0, N):
            board[i] = str(i) + board[i] + '\n'
        board = ' ' + ''.join([str(i) for i in (range(0, N))]) + '\n' + ''.join(board)
        print(board)
        user_op = input("Enter move location or -1 to pass")
        if user_op == '-1':
            return None
        else:
            fc = flatten([int(i) for i in user_op.split(',')])
            return self.color, fc
