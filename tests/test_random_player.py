import re
import unittest
from go_implementation.players.random_player import RandomPlayer
from go_implementation.base_implementation.go_sets import N, NN, WHITE, BLACK, EMPTY


def load_board(string):
    return re.sub(r'[^XO\.]+', '', string)


EMPTY_ROW = EMPTY * N


class TestActionsGeneration(unittest.TestCase):
    def test_empty_positions(self):
        player = RandomPlayer(WHITE)
        board = load_board(BLACK + EMPTY * (N-1) + BLACK + EMPTY * (N-1) + EMPTY_ROW * (N-2))
        empty_positions = player.empty_positions(board)
        # two black stones already on the board
        self.assertEqual(len(empty_positions), NN-2)
        # first empty position at 1 index location
        self.assertEqual(empty_positions[0], (EMPTY, 1))

    def test_possible_actions(self):
        player = RandomPlayer(WHITE)
        board = load_board(EMPTY + BLACK + EMPTY * (N-2) + BLACK + EMPTY * (N-1) + EMPTY_ROW * (N-2))
        possible_actions = player.possible_actions(board)
        # White can't move into the suicide spot thus minus three including the two black
        self.assertEqual(len(possible_actions), NN-3)
        # The two location is the first valid move for white
        self.assertEqual(possible_actions[0], (EMPTY, 2))

    def test_can_get_move(self):
        player = RandomPlayer(WHITE)
        board = load_board(EMPTY + BLACK + EMPTY * (N-2) + BLACK + EMPTY * (N-1) + EMPTY_ROW * (N-2))
        move = player.get_move(board)
        self.assertNotEqual(move, None)
        # white has a move at some position
        self.assertEqual(move[0], WHITE)

    def test_can_not_get_move(self):
        player = RandomPlayer(WHITE)
        board = load_board(EMPTY + BLACK*(N-1) + BLACK + EMPTY + BLACK*(N-2) + BLACK*N*(N-2))
        move = player.get_move(board)
        # There are no possible moves for white
        self.assertEqual(move, None)