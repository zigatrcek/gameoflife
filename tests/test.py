import unittest
import numpy as np

import game.Board

class Test_Board(unittest.TestCase):

    def setUp(self):
        self.zeros = Board([[0 for x in range(10)] for y in range(10)])
        self.ones = Board([[1 for x in range(10)] for y in range(10)])
        self.random = Board([[0, 1, 1], [0, 0, 1], [0, 1, 0]])
    
    def test_neighbours(self):
        self.assertEqual(self.zeros.neighbours(0, 0), 0)
        self.assertEqual(self.ones.neighbours(3, 0), 8)
        self.assertEqual(self.random.neighbours(1, 1), 4)
        
