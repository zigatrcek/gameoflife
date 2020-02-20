import numpy as np
import random

class Board:
    def __init__(self, width, heigth, board=None):
        self.width = width
        self.height = heigth
        if (board is None):
            self.board = np.random.randint(low = 2, size = (width, heigth))
        else:
            self.board = board


    def neighbours(self, row, column):
        return int(self.board[(row + 1) % self.height][column]
                 + self.board[(row - 1) % self.height][column]
                 + self.board[(row + 1) % self.height][(column + 1) % self.width]
                 + self.board[(row - 1) % self.height][(column + 1) % self.width]
                 + self.board[(row + 1) % self.height][(column - 1) % self.width]
                 + self.board[(row - 1) % self.height][(column - 1) % self.width]
                 + self.board[row][(column + 1) % self.width]
                 + self.board[row][(column - 1) % self.width])

    
    def run(self, iterations=1):
        self.new_board = self.board.copy()

        for row, column in np.ndindex(self.board.shape):
            neighbour_count = self.neighbours(row, column)
            if (neighbour_count < 2 or neighbour_count > 3):  # Manj kot 2 ali več kot 3 sosedje -> umre
                self.new_board[row][column] = 0
            elif (neighbour_count == 3):  # Točno trije sosedje -> (o)živi
                self.new_board[row][column] = 1

        self.board = self.new_board
        

    def __str__(self):
        return str(self.board) + '\n'

