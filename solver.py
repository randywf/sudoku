import numpy as np
from board import Board



class Solver(Board):
    def __init__(self, size):
        Board.__init__(self, size)



if __name__ == '__main__':
    t = Solver(3)
    print(t.available_cells)
    t.start()
    print(t.available_cells)
    print(t.history)
    t.print()