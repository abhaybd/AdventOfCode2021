def read_data(file):
    with open(file) as f:
        lines = f.read().split("\n")
    return [list(map(int, line)) for line in lines]

def get_neighbors(n_rows, n_cols, row, col):
    neighbors = []
    if row > 0:
        neighbors.append((row-1, col))
    if row < n_rows - 1:
        neighbors.append((row+1, col))
    if col > 0:
        neighbors.append((row, col-1))
    if col < n_cols - 1:
        neighbors.append((row, col+1))
    return neighbors

def is_low(heights, row, col):
    h = heights[row][col]
    return all(h < heights[r][c] for r, c in get_neighbors(len(heights), len(heights[row]), row, col))

def get_low_points(heights):
    lows = []
    for r in range(len(heights)):
        for c in range(len(heights[r])):
            if is_low(heights, r, c):
                lows.append((r, c))
    return lows

def basin_size(heights, row, col, visited=None):
    if visited is None:
        visited = set()
        visited.add((row, col))
    h = heights[row][col]
    size = 1
    for n in get_neighbors(len(heights), len(heights[row]), row, col):
        r, c = n
        if h < heights[r][c] < 9 and n not in visited:
            visited.add(n)
            size += basin_size(heights, r, c, visited)
    return size

def main():
    heights = read_data("input.txt")
    lows = get_low_points(heights)
    basin_sizes = [basin_size(heights, r, c) for r, c in lows]
    size_prod = 1
    for size in sorted(basin_sizes)[-3:]:
        size_prod *= size
    print(size_prod)

main()
