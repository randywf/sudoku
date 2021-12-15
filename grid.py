def _get_box(row, col):
    pass

class grid:
    def __init__(self, grid_size=9):
        self.grid_size = grid_size
        self.grid_rows = {row:{col:0 for col in range(self.grid_size)} for row in range(self.grid_size)}
        self.grid_cols = {col:{row:0 for row in range(self.grid_size)} for col in range(self.grid_size)}
        self.grid_boxes = {box:{cell:0 for cell in range(self.grid_size)} for box in range(self.grid_size)}
        
    def get_box(self, row, col):
        return (col // (self.grid_size // 3)) + ((row // (self.grid_size // 3)) * (self.grid_size // 3))

    #TODO: Redundant with new data structures. Remove? 
    def get_box_values(self, box):
        row_offset = (box // (self.grid_size // 3)) * (self.grid_size // 3)
        col_offset = (box % (self.grid_size // 3)) * (self.grid_size // 3)
        box = [[0 for i in range(self.grid_size // 3)] for j in range(self.grid_size // 3)]
        for i in range(self.grid_size):
            sub_row = self.grid[row_offset + i, col_offset : col_offset + self.grid_size]
            box.append()
        return box

    def row_col_to_box_cell(self, row, col):
        box = self.get_box(row, col)
        row_offset = (box // (self.grid_size // 3)) * (self.grid_size // 3)
        col_offset = (box % (self.grid_size // 3)) * (self.grid_size // 3)
        cell = (col - col_offset) + (row - row_offset) * (self.grid_size // 3)
        return (box, cell)

    def update_cell(self, row, col, val):
        self.grid_rows[row][col] = val
        self.grid_cols[col][row] = val
        box, cell = self.row_col_to_box_cell(row, col)
        self.grid_boxes[box][cell] = val

    def reset_cell(self, row, col):
        self.grid_rows[row][col] = 0
        self.grid_cols[col][row] = 0
        box, cell = self.row_col_to_box_cell(row, col)
        self.grid_boxes[box][cell] = 0

    #TODO: Put this someplace else
    def display_grid(self):
        for m in range(self.grid_size):
            if m % (self.grid_size // 3) == 0:
                h = "="
            else:
                h = '-'
            for n in range(self.grid_size):
                print(h * 4, end="")
            print(h)
            for n in range(self.grid_size):
                if n % (self.grid_size // 3) == 0:
                    v = "║"
                else:
                    v = "│"
                
                if (self.grid_rows[m][n] == 0):
                    print(f"{v}   ", end="")
                else:
                    print(f"{v} {self.grid_rows[m][n]} ", end="")
            print(v)
        for n in range(self.grid_size):
            print(h * 4, end="")
        print(h)
