import time
from GameOfLife import GameOfLife

if (__name__ == '__main__'):
    width = int(input('Width: '))
    height = int(input('Height: '))
    iterations = int(input('Iterations: '))

    game = GameOfLife(width, height)

    with open("output.txt","w") as f:
        f.write(str(height) + '\n')
        t1 = time.time()
        for i in range(iterations):
            f.write(str(game))
            game.run()
        t2 = time.time()
        
    print('Seconds:', t2 - t1)

