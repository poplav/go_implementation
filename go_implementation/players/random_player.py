from go_implementation.players.utils import possible_actions, should_pass
import random


class RandomPlayer:

    def __init__(self, color):
        self.color = color
        self.ko = None

    def get_move(self, board):
        actions = possible_actions(board, self.color, self.ko)
        if len(actions) > 0 and not should_pass(board, self.color, self.ko):
            return self.color, random.choice(actions)[1]
        else:
            return None


