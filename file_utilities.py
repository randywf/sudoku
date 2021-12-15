import json

from grid import grid

def load_from_csv(filename):
    with open(filename, 'r') as f:
        data = f.read()
    new_grid = grid()
    for row, row_str in enumerate(data.split('\n')):
        for col, cell_str in enumerate(row_str.split(',')):
            new_grid.update_cell(row, col, int(cell_str))
    return new_grid

def save_to_csv(grid, filename):
    with open(filename, 'w') as f:
        for row in range(grid.grid_size):
            for col in range(grid.grid_size):
                f.write(str(grid.grid_rows[row][col]))
                if col < grid.grid_size - 1:
                    f.write(',')
            if row < grid.grid_size - 1:
                f.write('\n')

def load_from_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    new_grid = grid()
    for row_str in data.keys():
        for col_str, cell_str in data[row_str].items():
            new_grid.update_cell(int(row_str), int(col_str), int(cell_str))
    return new_grid

def save_to_json(grid, filename):
    with open(filename, 'w') as f:
        json.dump(grid.grid_rows, f)
