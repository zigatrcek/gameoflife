from Board import Board
import time

if (__name__ == '__main__'):
    print('Width: ', end='')
    width = int(input())
    print('Height: ', end='')
    height = int(input())
    print('Num. of iterations: ', end='')
    iterations = int(input())

    board = Board(width, height)
    with open("output.txt","w") as f:
        f.write(str(height) + '\n')
        t1 = time.time()
        for i in range(iterations):
            f.write(str(board))
            board.run()
        t2 = time.time()
    print('Seconds:', t2 - t1)









