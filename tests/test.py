import unittest

from game.GameOfLife import GameOfLife

class Test_Board(unittest.TestCase):

    def setUp(self):
        self.zeros = GameOfLife([[0 for x in range(10)] for y in range(10)])
        self.ones = GameOfLife([[1 for x in range(10)] for y in range(10)])
        self.random = GameOfLife([[0, 1, 1], [0, 0, 1], [0, 1, 0]])
    
    def test_neighbours(self):
        self.assertEqual(self.zeros.neighbours(0, 0), 0)
        self.assertEqual(self.ones.neighbours(3, 0), 8)
        self.assertEqual(self.random.neighbours(1, 1), 4)
        
