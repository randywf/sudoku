import numpy as np

class Board:
    def __init__(self, size):
        self.size = size
        self.side = size * size
        # 2D Numpy array that stores all values on board (row, col indexed)
        self.board = np.full((self.side, self.side), 0, dtype="int")
        # Dictionaries to access values
        self.rows = {m: self.board[m, :] for m in range(self.side)}
        self.columns = {n : self.board[:, n] for n in range(self.side)}
        self.squares = {s: self.get_square(s) for s in range(self.side)}
        # Dictionaries to store counts of values
        self.counts_rows = {}
        self.counts_columns = {}
        self.counts_squares = {}
        for i in range(self.side):
            for j in range(self.side):
                self.counts_rows[(i, j + 1)] = 0
                self.counts_columns[(i, j + 1)] = 0
                self.counts_squares[(i, j + 1)] = 0
                
    
    def get_square(self, s):
        """
        get_square is necessary because Numpy can't return a view of multiple
        slices of an array. This way, the squares are recaculated when they
        need to be.
        """
        # row_offset and col_offset give the upper left tile of the square.
        row_offset = (s // self.size) * self.size
        col_offset = (s % self.size) * self.size
        square = np.empty(0, dtype="int")
        # Create sub rows for each row in the square, then combine together
        for i in range(self.size):
            sub_row = self.board[row_offset + i,
                                 col_offset : col_offset + self.size]
            square = np.append(square, sub_row)
        return square


    def set_value(self, m, n, v):
        """
        Sets a value on the sudoku board at the m'th row, n'th column, with a
        value of v. This method updates attributes that keep count of the
        number of any value (i.e. how many 9s?) in rows, columns and squares.
        Use this instead of trying to directly set values in the matrix.
        """
        # If same value, return
        if (v == self.board[m, n]):
            return
        # Find what square this tile belongs to
        s = (n // self.size) + (m // self.size * self.size)
        # Update counts
        # Changing a value, decrement count of previous value
        if (self.board[m, n] != 0):
            self.counts_rows[m, self.board[m, n]] -= 1
            self.counts_columns[n, self.board[m, n]] -= 1
            self.counts_squares[s, self.board[m, n]] -= 1
        # Increment count of new value
        self.counts_rows[m, v] += 1
        self.counts_columns[n, v] += 1
        self.counts_squares[s, v] += 1
        # Update board
        self.board[m, n] = v
        self.squares[s] = self.get_square(s)


    def load_csv(self, filename):
        """
        Loads a board from a CSV file.
        """
        # Read data from file
        with open(filename, "r") as file:
            rows = file.readlines()
            for i, row in enumerate(rows):
                nums = row.rstrip().split(',')
                for j, num in enumerate(nums):
                    self.set_value(i, j, int(num))


    def validate_row(self, m):
        """
        Checks that a row m has one count of each value.
        """
        for i in range(1, self.side + 1):
            if self.counts_rows[m, i] != 1:
                return False
        return True
    

    def validate_column(self, n):
        """
        Checks that a column n has one count of each value.
        """
        for i in range(1, self.side + 1):
            if self.counts_columns[n, i] != 1:
                return False
        return True


    def validate_square(self, s):
        """
        Checks that a square s has one count of each value.
        """
        for i in range(1, self.side + 1):
            if self.counts_squares[s, i] != 1:
                return False
        return True
    

    def validate(self):
        """
        Validates every row, column, and square on the board, using validation
        methods.
        """
        # Check rows
        for m in range(self.side):
            if not self.validate_row(m):
                return False
        # Check columns
        for n in range(self.side):
            if not self.validate_column(n):
                return False
        # Check squares
        for s in range(self.size):
            if not self.validate_square(s):
                return False
        # Passed all checks
        return True
        

    def print(self):
        """
        Prints the current state of the board to STDOUT.
        """
        for m in range(self.side):
            if m % self.size == 0:
                h = "="
            else:
                h = '-'

            for n in range(self.side):
                print(h * 4, end="")
            print(h)
            
            for n in range(self.side):
                if n % self.size == 0:
                    v = "║"
                else:
                    v = "│"
                
                if (np.isnan(self.board[m,n])):
                    print(f"{v}   ", end="")
                else:
                    print(f"{v} {self.board[m,n]} ", end="")
            print(v)
        
        for n in range(self.side):
            print(h * 4, end="")
        print(h)
