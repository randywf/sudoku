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
        row_offset = (s // self.size) * self.size
        col_offset = (s % self.size) * self.size
        square = np.empty(0, dtype="int")

        for i in range(self.size):
            sub_row = self.board[row_offset + i, col_offset : col_offset + self.size]
            square = np.append(square, sub_row)

        return square


    def set_value(self, m, n, v):
        # If same value, return
        if (v == self.board[m, n]):
            return

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

        self.board[m, n] = v
        self.squares[s] = self.get_square(s)


    def load_csv(self, filename):
        # Read data from file
        with open(filename, "r") as file:
            rows = file.readlines()
            for i, row in enumerate(rows):
                nums = row.rstrip().split(',')
                for j, num in enumerate(nums):
                    self.set_value(i, j, int(num))


    def validate_row(self, m):
        for i in range(self.side):
            if not i in self.board[m, :]:
                return (False, i)
        return (True, None)
    

    def validate_column(self, n):
        for i in range(self.side):
            if not i in self.board[:, n]:
                return (False, i)
        return (True, None)


    def validate_square(self, s):
        row_offset = (s // self.size) * self.size
        col_offset = (s % self.size) * self.size
        square = np.empty(0, dtype="int")

        for i in range(self.size):
            sub_row = self.board[row_offset + i, col_offset : col_offset + self.size]
            square = np.append(square, sub_row)

        for i in range(self.side):
            if not i in square:
                return (False, i)
        return (True, None)
    

    def validate(self):
        # Check rows
        for m in range(self.side):
            continue
        # Check columns
        for n in range(self.side):
            if not self.validate_column(m):
                return False
        # Check squares
        for s in range(self.size):
            if not self.validate_square(s):
                return False
        # Passed all checks
        return True


    def gen_mc(self):
        random_indices = np.random.randint((1,1), self.side)
        random_number = np.random.randint(self.side) + 1
        self.board[random_indices[0], random_indices[1]] = random_number


    def print(self):
        
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



if __name__ == "__main__":
    test_board = Board(2)
    test_board.load_csv("4x4_valid.csv")

    test_board.print()
    print(test_board.rows[0])
    print(test_board.columns[0])
    print(test_board.squares[0])
    print(test_board.counts_rows)
    print(test_board.counts_columns)
    print(test_board.counts_squares)
    print(test_board.validate())

    test_board.set_value(0,0,1)
    test_board.print()
    print(test_board.rows[0])
    print(test_board.columns[0])
    print(test_board.squares[0])
    print(test_board.counts_rows)
    print(test_board.counts_columns)
    print(test_board.counts_squares)
    print(test_board.validate())