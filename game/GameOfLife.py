import numpy as np

class GameOfLife:
    """
    A class that represends a board of Conways Game of Life.

    Attributes:
        width (int): The width of the board.
        heighth (int): The heigth of the board
        board (list): Optional start state of the board.
    """
    
    def __init__(self, width, heigth, board=None):
        """
        The constructor of the Board class.

        Parameters:
            width (int): The width of the board.
            heighth (int): The heigth of the board
            board (list): Optional start state of the board.
        """

        self.width = width
        self.height = heigth
        if (board is not None): 
            self.board = np.array(board)
        else:
            self.board = np.random.randint(low = 2, size = (width, heigth))
            

    def cell_neighbours(self, row, column):
        """
        The function to count the number of active neighbours of a cell.

        Parameters:
            row (int): The row coordinate of the cell.
            column (int): The column coordinate of the cell.

        Returns:
            Integer count of the active neighbours of the cell.
        """

        # Redeclaring common attributes to local variables for faster access
        board = self.board
        height = self.height
        width = self.width
        
        # A sum of the neighbouring values of the cell, hardcoded for speed
        return int(board[(row + 1) % height][(column - 1) % width]  # Top left
                 + board[(row - 1) % height][column]                # Top center
                 + board[(row + 1) % height][(column + 1) % width]  # Top right
                 + board[row][(column - 1) % width]                 # Center left
                 + board[row][(column + 1) % width]                 # Center right
                 + board[(row - 1) % height][(column - 1) % width]  # Bottom left
                 + board[(row + 1) % height][column]                # Bottom center
                 + board[(row - 1) % height][(column + 1) % width]) # Bottom right

    
    def run(self, iterations=1):
        """
        The function to run one or more iterations of the game.

        Parameters:
            iterations (int): The number of iterations to run.
        """

        # Copy the current board to a new board
        # Removes the need to check previous values in the case of two active neighbours
        new_board = self.board.copy()

        for _ in range(iterations):
            for row, column in np.ndindex(self.board.shape):
                neighbour_count = self.cell_neighbours(row, column)
                # A cell with < 2 or > 3 neighbours will always become inactive
                if (neighbour_count < 2 or neighbour_count > 3):
                    new_board[row][column] = 0
                # A cell with exactly three neighbours will always become active
                elif (neighbour_count == 3):
                    new_board[row][column] = 1
            self.board = new_board
        

    def __str__(self):
        pyboard = self.board.tolist()
        output = '\n'.join(' '.join(str(cell) for cell in row) for row in self.board) + '\n'
        return output

        



