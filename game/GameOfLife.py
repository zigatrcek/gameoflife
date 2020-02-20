from Board import Board

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
        for i in range(iterations):
            f.write(str(board))
            board.iterate()









