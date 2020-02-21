import unittest

import game
from game.GameOfLife import GameOfLife


class Test_GameOfLife(unittest.TestCase):
    """
    Run tests from root with the command:
        'python3 -m unittest tests.test.Test_GameOfLife'
    """

    def setUp(self):
        self.zeros = GameOfLife(10, 10, [[0 for x in range(10)] for y in range(10)])
        self.ones = GameOfLife(10, 10, [[1 for x in range(10)] for y in range(10)])
        self.random = GameOfLife(3, 3, [[0, 1, 1], [0, 0, 1], [0, 1, 0]])
    
    def test_neighbours(self):
        result_zeros = self.zeros.cell_neighbours(0, 0)
        result_ones = self.ones.cell_neighbours(3, 0)
        result_random = self.random.cell_neighbours(1, 1)

        self.assertEqual(result_zeros, 0)
        self.assertEqual(result_ones, 8)
        self.assertEqual(result_random, 4)
    
    def test_init(self):
        self.assertRaises(ValueError, GameOfLife, -2, 5)
        self.assertRaises(ValueError, GameOfLife, 5, -2)
        