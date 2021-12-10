from collections import deque

OPEN = set("<{[(")
PAIRS = {"<": ">", "{": "}", "[": "]", "(": ")"}
POINTS = {">": 25137, "}": 1197, "]": 57, ")": 3}

def read_data(file):
    with open(file) as f:
        return f.read().split("\n")

def get_corruption(line):
    stack = deque()
    for c in line:
        if c in OPEN:
            stack.append(c)
        else:
            if len(stack) == 0 or c != PAIRS[stack.pop()]:
                return c
    return None

def main():
    lines = read_data("input.txt")
    print(sum(POINTS[c] for c in map(get_corruption, lines) if c is not None))

main()
