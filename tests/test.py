import unittest
from copy import deepcopy
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from src.helper import merge_values, go_up, down, left, right


class TestPrivate2048(unittest.TestCase):
    def test_merge_values(self):
        input_grid = [[0, 0, 2, 2], [16, 8, 8, 0], [64, 2, 0, 2], [2, 0, 0, 0]]
        result_from_merge_values = merge_values(input_grid)
        result = ([[0, 0, 4, 0], [16, 16, 0, 0], [64, 2, 0, 2], [2, 0, 0, 0]], True)
        self.assertTrue(result_from_merge_values == result)

    def test_up(self):
        input_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2], [2, 0, 0, 0]]
        result_from_up = go_up(input_grid)
        result = ([[2, 0, 0, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], True)
        self.assertTrue(result_from_up == result)

    def test_down(self):
        input_grid = [[0, 4, 0, 32], [8, 2, 0, 0], [4, 0, 0, 16], [256, 0, 0, 0]]
        result_from_down = down(input_grid)
        result = ([[0, 0, 0, 0], [8, 0, 0, 0], [4, 4, 0, 32], [256, 2, 0, 16]], True)
        self.assertTrue(result_from_down == result)

    def test_right(self):
        input_grid = [[2, 16, 8, 8], [4, 128, 16, 32], [64, 8, 2, 2], [2, 0, 0, 0]]
        result_from_right = right(input_grid)
        result = ([[0, 2, 16, 16], [4, 128, 16, 32], [0, 64, 8, 4], [0, 0, 0, 2]], True)
        self.assertTrue(result_from_right == result)

    def test_left(self):
        input_grid = [[4, 0, 128, 0], [2, 16, 0, 0], [0, 16, 0, 2], [2, 16, 0, 0]]
        result_from_left = left(input_grid)
        result = ([[4, 128, 0, 0], [2, 16, 0, 0], [16, 2, 0, 0], [2, 16, 0, 0]], True)
        self.assertTrue(result_from_left == result)


if __name__ == '__main__':
    unittest.main(verbosity=2)