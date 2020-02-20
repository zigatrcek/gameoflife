from game.Board import Board
import time

if (__name__ == '__main__'):
    width = int(input('Width: '))
    height = int(input('Height: '))
    iterations = int(input('Iterations: '))

    board = Board(width, height)

    with open("output.txt","w") as f:
        f.write(str(height) + '\n')
        t1 = time.time()
        for i in range(iterations):
            f.write(str(board))
            board.run()
        t2 = time.time()
        
    print('Seconds:', t2 - t1)









