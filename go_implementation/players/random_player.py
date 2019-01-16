from go_implementation.base_implementation.go_sets import Position, WHITE, BLACK, EMPTY, IllegalMove, LibertyTracker
import random


def is_valid_move(board, fc, color, ko):
    try:
        Position(board=board, ko=ko, liberty_tracker=LibertyTracker.from_board(board)).play_move(fc[1], color)
        return True
    except IllegalMove:
        return False


def empty_positions(board):
    return [fc for fc in zip(board, range(0, len(board))) if fc[0] == EMPTY]


def possible_actions(board, color, ko):
    return [action for action in empty_positions(board) if is_valid_move(board, action, color, ko)]


class RandomPlayer:

    def __init__(self, color):
        self.color = color
        self.ko = None

    def get_move(self, board):
        actions = possible_actions(board, self.color, self.ko)
        if len(actions) > 0 and not self.should_pass(board):
            return self.color, random.choice(actions)[1]
        else:
            return None

    def should_pass(self, board):
        if 'O' not in board and 'X' not in board:
            return False
        simulate_positions = Position(board=board, ko=self.ko, liberty_tracker=LibertyTracker.from_board(board))
        score = simulate_positions.score()
        player_score = score if self.color == BLACK else score*-1
        opponent_color = WHITE if self.color == BLACK else WHITE
        # while player_score > 0 and the opponent can make moves do moves and check if you win no matter what
        opponent_possible_actions = possible_actions(simulate_positions.get_board(), opponent_color,
                                                     simulate_positions.ko)
        while player_score > 0 and len(opponent_possible_actions) > 0:
            opponent_action_location = random.choice(opponent_possible_actions)[1]
            simulate_positions = simulate_positions.play_move(opponent_action_location, opponent_color)
            score = simulate_positions.score()
            player_score = score if self.color == BLACK else score * -1
            opponent_possible_actions = possible_actions(simulate_positions.get_board(), opponent_color,
                                                         simulate_positions.ko)
        return player_score > 0
