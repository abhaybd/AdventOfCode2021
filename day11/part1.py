import numpy as np

def read_data(file):
    with open(file) as f:
        lines = f.read().split("\n")
    grid = [[int(c) for c in line] for line in lines]
    return np.array(grid)

def get_neighbors(grid, row, col):
    neighbors = []
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if r == row and col == c:
                continue
            if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
                neighbors.append((r,c))
    return neighbors

def flash(grid, flashing, row, col):
    for r, c in get_neighbors(grid, row, col):
        if not flashing[r][c]:
            grid[r][c] += 1
            if grid[r][c] > 9:
                flashing[r][c] = True
                flash(grid, flashing, r, c)

def main():
    grid = read_data("input.txt")
    n_flashed = 0
    for _ in range(100):
        grid += 1
        flashing = grid > 9
        to_flash = []
        for r in range(len(flashing)):
            for c in range(len(flashing[r])):
                if flashing[r][c]:
                    to_flash.append((r, c))
        for r, c in to_flash:
            flash(grid, flashing, r, c)
        n_flashed += flashing.sum()
        grid[flashing] = 0
    print(n_flashed)

main()
