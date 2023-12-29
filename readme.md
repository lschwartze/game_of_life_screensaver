## screensaver based on Conway's Game of Life

The codes stored in this repository play Game of Life on a random starting position. Using auto-py-to-exe the file game_of_life.py was converted to an exe file which can be further renamed to a .scr file which windows can use as a screensaver.
The drawing is handled by pygame which also allows us to cancel execution once any user interaction was detected.

board.py defines the class that handles the game board and all calculations and drawings.
game_of_life.py is only here to start execution and to define a board size that is suited for the screen size. In my case, the screen's format is 1280x720 so the game is played with 128*720 cells of size 10x10.