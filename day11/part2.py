def read_data(file):
    with open(file) as f:
        lines = f.read().split("\n")
    grid = [[int(c) for c in line] for line in lines]
    return grid

def get_neighbors(grid, row, col):
    neighbors = []
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if r == row and col == c:
                continue
            if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
                neighbors.append((r,c))
    return neighbors

def flash(grid, flashing: set, row, col):
    for r, c in get_neighbors(grid, row, col):
        if (r, c) not in flashing:
            grid[r][c] += 1
            if grid[r][c] > 9:
                flashing.add((r, c))
                flash(grid, flashing, r, c)

def main():
    grid = read_data("input.txt")
    i = 0
    done = False
    while not done:
        to_flash = set()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                grid[r][c] += 1
                if grid[r][c] > 9:
                    to_flash.add((r, c))
        for r, c in list(to_flash):
            flash(grid, to_flash, r, c)
        for r, c in to_flash:
            grid[r][c] = 0
        done = len(to_flash) == sum(map(len, grid))
        i += 1
    print(i)

main()
