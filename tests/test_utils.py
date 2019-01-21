import re
import unittest
from go_implementation.base_implementation.go_sets import WHITE, BLACK, EMPTY, get_valid_neighbors
from go_implementation.players.utils import should_pass

import go_implementation.base_implementation.go_sets
go_implementation.base_implementation.go_sets.N=3
go_implementation.base_implementation.go_sets.NN=9
go_implementation.base_implementation.go_sets.NEIGHBORS = [get_valid_neighbors(fc) for fc in range(9)]


def load_board(string):
    return re.sub(r'[^XO\.]+', '', string)


class TestPlayerUtils(unittest.TestCase):
    def test_should_pass_not_immediate(self):
        """
        O..
        OX.
        .OO
        Should not pass as black can overtake by playing/eventually win
        """
        board = load_board(
            WHITE + EMPTY*2 +
            WHITE + BLACK + EMPTY +
            EMPTY + WHITE*2
        )
        result = should_pass(board, WHITE, None)
        self.assertEqual(result, False)

    def test_should_pass_immediate(self):
        """
        O..
        OXX
        .OO
        Should not pass as black can overtake by playing/eventually win
        """
        board = load_board(
            WHITE + EMPTY*2 +
            WHITE + BLACK*2 +
            EMPTY + WHITE*2
        )
        result = should_pass(board, WHITE, None)
        self.assertEqual(result, False)
