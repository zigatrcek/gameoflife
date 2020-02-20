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


    def neighbours(self, row, collumn):
        neighbour_count = 0
        for current_row in range(row - 1, row + 2):
                for current_collumn in range(collumn - 1, collumn + 2):
                    if (current_collumn != collumn and current_row != row):  # Ne šteje sam sebe
                        neighbour_count += self.board[current_row % self.height][current_collumn % self.width]
        return neighbour_count

    
    def run(self, iterations=1):
        self.new_board = self.board.copy()

        for row, collumn in np.ndindex(self.board.shape):
            neighbour_count = self.neighbours(row, collumn)
            if (neighbour_count < 2 or neighbour_count > 3):  # Manj kot 2 ali več kot 3 sosedje -> umre
                self.new_board[row][collumn] = 0
            elif (neighbour_count == 3):  # Točno trije sosedje -> (o)živi
                self.new_board[row][collumn] = 1

        self.board = self.new_board
        

    def __str__(self):
        return str(self.board) + '\n'

