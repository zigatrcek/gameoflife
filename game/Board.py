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
        # Deklaracija lokalnih spremenljivk zaradi hitrejšega dostopa
        board = self.board
        height = self.height
        width = self.width
        
        return int(board[(row + 1) % height][column]
                 + board[(row - 1) % height][column]
                 + board[(row + 1) % height][(column + 1) % width]
                 + board[(row - 1) % height][(column + 1) % width]
                 + board[(row + 1) % height][(column - 1) % width]
                 + board[(row - 1) % height][(column - 1) % width]
                 + board[row][(column + 1) % width]
                 + board[row][(column - 1) % width])

    
    def run(self, iterations=1):
        new_board = self.board.copy()

        for _ in range(iterations):
            for row, column in np.ndindex(self.board.shape):
                neighbour_count = self.neighbours(row, column)
                if (neighbour_count < 2 or neighbour_count > 3):  # Manj kot 2 ali več kot 3 sosedje -> umre
                    new_board[row][column] = 0
                elif (neighbour_count == 3):  # Točno trije sosedje -> (o)živi
                    new_board[row][column] = 1

            self.board = new_board
        

    def __str__(self):
        pyboard = self.board.tolist()
        output = '\n'.join(' '.join(str(cell) for cell in row) for row in self.board) + '\n'
        return output

        



