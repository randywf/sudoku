import numpy as np

class Board:
    def __init__(self, size):
        self.size = size
        self.side = size * size
        self.board = np.full((self.side, self.side), 0, dtype="int")
    
    def load_csv(self, filename):
        with open(filename, "r") as file:
            rows = file.readlines()
            for i, row in enumerate(rows):
                nums = row.rstrip().split(',')
                for j, num in enumerate(nums):
                    self.board[i,j] = int(num)
            
    def validate_row(self, m):
        for i in range(self.side):
            if not i in self.board[m, :]:
                return False
        return True
    
    def validate_column(self, n):
        for i in range(self.side):
            if not i in self.board[:, n]:
                return False
        return True

    def validate_square(self, s):
        row_offset = (s // self.size) * self.size
        col_offset = (s % self.size) * self.size
        square = np.empty(0, dtype="int")

        for i in range(self.size):
            sub_row = self.board[row_offset + i, col_offset : col_offset + self.size]
            square = np.append(square, sub_row)

        for i in range(self.side):
            if not i in square:
                return False
        return True
    
    def validate(self):
        # Check rows
        for m in range(self.side):
            if not self.validate_row(m):
                return False
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