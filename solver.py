import random
import numpy as np
from numpy.core.fromnumeric import sort
from board import Board



class Solver(Board):
    
    def __init__(self, size):
        Board.__init__(self, size)
        self.available_cells = {}

        for m in range(self.side):
            for n in range(self.side):
                # True value is just a placeholder, we're interested in keys
                self.available_cells[(m,n)] = True

        row_ind = np.arange(9)
        col_ind = np.arange(9)
        np.random.shuffle(row_ind)
        np.random.shuffle(col_ind)
        for i in range(9):
            self.set_value(row_ind[i], col_ind[i], i)
            self.available_cells.pop((row_ind[i], col_ind[i]))
    

    def next_available_cell(self):
        if len(self.available_cells) == 0:
            return (-1,-1)
        else:
            cells = list(self.available_cells.keys())
            cells.sort(key=lambda y: y[0])
            return cells[0]
    

    def is_value_allowed(self, m, n, v):
        s = self.get_square(m, n)
        if self.counts_rows[m, v] != 0:
            return False
        if self.counts_columns[n, v] != 0:
            return False
        if self.counts_squares[s, v] != 0:
            return False
        return True
    

    def solve(self):
        cell = self.next_available_cell()

        if cell == (-1,-1):
            # Make final assignment
            for c in self.counts_rows.items():
                if c[1] == 0:
                    m = c[0][0]
                    v = c[0][1]
            for c in self.counts_columns.items():
                if c[1] == 0:
                    n = c[0][0]
            self.set_value(m, n, v)

            return True
        
        for i in range(1, self.side + 1):
            if self.is_value_allowed(cell[0], cell[1], i):
                # Make assignment
                self.set_value(cell[0], cell[1], i)
                self.available_cells.pop((cell[0], cell[1]))
                # Recurse to check if this branch of search works
                if self.solve():
                    return True
                # Didn't work, undo assignment
                self.reset_value(cell[0], cell[1])
                self.available_cells[(cell[0], cell[1])] = True
        
        # Backtrack up the search tree
        return False
    
    def swap_numbers(self):
        shuffled_numbers = np.arange(1, self.side + 1)
        np.random.shuffle(shuffled_numbers)
        for m in range(self.side):
            for n in range(self.side):
                new_value = shuffled_numbers[self.board[m, n] - 1]
                self.board[m, n] = new_value


if __name__ == '__main__':
    t = Solver(3)
    t.print()
    t.solve()
    t.print()
    if t.validate():
        print("Valid solution generated")
    else:
        print("Invalid solution")

    t.swap_numbers()
    t.print()
    print("Numbers have been swapped")

    t.recount_values()
    if t.validate():
        print("Solution is still valid after recount")
    else:
        print("Error")