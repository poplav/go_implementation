from go_implementation.base_implementation.go_sets import Position, WHITE, BLACK, LibertyTracker
from go_implementation.players.utils import possible_actions, should_pass


class MaximalNextScorePlayer:

    def __init__(self, color):
        self.color = color
        self.ko = None

    def get_move(self, board):
        actions = possible_actions(board, self.color, self.ko)
        if len(actions) > 0 and not should_pass(board, self.color, self.ko):
            position = Position(board=board, ko=self.ko, liberty_tracker=LibertyTracker.from_board(board))
            current_score = position.score()
            player_current_score = current_score if self.color == BLACK else current_score*-1
            maximal_score, maximal_fc = player_current_score, -1
            for action in actions:
                action_score = position.play_move(action[1], self.color).score()
                player_action_score = action_score if self.color == BLACK else action_score*-1
                if player_action_score >= maximal_score:
                    maximal_score = player_action_score
                    maximal_fc = action[1]
            return self.color, maximal_fc
        else:
            return None
