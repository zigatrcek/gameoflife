# Game of life

Pyhton implementation of Conway's Game of life.

## Rules

 ### Standard rules
 ```
1. Any live cell with two or three neighbors survives.
2. Any dead cell with three live neighbors becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.
```
 ### Special rule
 ```
 * Neighbours of cells on the edge wrap around the board.
```

## Usage

```python

 game = GameOfLife(10, 15)                              # Creates a game of life board with width 10 and height 15 (expects integer inputs).
 game = GameOfLife(3, 3, [[0, 1, 1], [0, 0, 0], [0, 1, 0]])   # Create a game of life board from a 2D dimensional list of 1 and 0.

 game.run()                                             # Runs the game of life for one iteration, returns the final state.
 game.run(5)                                            # Runs the game of life for a specified amount of iterations, returns the final state.
```
