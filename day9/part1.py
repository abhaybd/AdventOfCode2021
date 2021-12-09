def read_data(file):
    with open(file) as f:
        lines = f.read().split("\n")
    return [list(map(int, line)) for line in lines]

def is_low(heights, row, col):
    h = heights[row][col]
    if row > 0 and h >= heights[row-1][col]:
        return False
    if row < len(heights) - 1 and h >= heights[row+1][col]:
        return False
    if col > 0 and h >= heights[row][col-1]:
        return False
    if col < len(heights[row]) - 1 and h >= heights[row][col+1]:
        return False
    return True

def main():
    heights = read_data("input.txt")
    total_risk = 0
    for r in range(len(heights)):
        for c in range(len(heights[r])):
            if is_low(heights, r, c):
                total_risk += 1 + heights[r][c]
    print(total_risk)

main()
