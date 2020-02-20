import multiprocessing
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
        self.current_x, self.current_y = 0, 0  

    def neighbours(self, collumn, row):
        neighbour_count = 0
        for current_row in range(row - 1, row + 2):
                for current_collumn in range(collumn - 1, collumn + 2):
                    if (current_collumn != collumn and current_row != row):
                        neighbour_count += self.board[current_row % self.height][current_collumn % self.width]
        return neighbour_count

    def process_range(self, row_start, num_of_rows):
        for row in range(row_start, row_start + num_of_rows):
            for collumn in range(self.width):
                neighbour_count = self.neighbours(collumn, row)
                if (neighbour_count < 2 or neighbour_count > 3):  # Manj kot 2 ali več kot 3 sosedje -> umre
                    self.new_board[row][collumn] = 0
                elif (neighbour_count == 3):  # Točno trije sosedje -> oživi
                    self.new_board[row][collumn] = 1
    
    def iterate(self, iterations=1, batch_size=1, threads=1):
        self.new_board = self.board.copy()

        processes = []
        for _ in range(threads):
            p = multiprocessing.Process(target=self.process_range, args=[])
            processes.append(p)

        for _ in range(iterations):
            for process in processes:
                process.start()
            for process in processes:
                process.join()

            self.board = new_board
        

    def __str__(self):
        return str(self.board) + '\n'

