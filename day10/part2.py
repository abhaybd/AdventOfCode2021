from collections import deque

OPEN = set("<{[(")
PAIRS = {"<": ">", "{": "}", "[": "]", "(": ")"}
POINTS = {">": 4, "}": 3, "]": 2, ")": 1}

def read_data(file):
    with open(file) as f:
        return f.read().split("\n")

def is_corrupted(line):
    stack = deque()
    for c in line:
        if c in OPEN:
            stack.append(c)
        else:
            if len(stack) == 0 or c != PAIRS[stack.pop()]:
                return True
    return False

def autocomplete(line):
    stack = deque()
    for c in line:
        if c in OPEN:
            stack.append(c)
        else:
            stack.pop()
    complete = []
    while len(stack):
        complete.append(PAIRS[stack.pop()])
    return complete

def get_score(completion):
    score = 0
    for c in completion:
        score *= 5
        score += POINTS[c]
    return score

def main():
    lines = read_data("input.txt")
    incomplete = [line for line in lines if not is_corrupted(line)]
    scores = sorted(map(get_score, map(autocomplete, incomplete)))
    print(scores[len(scores)//2])

main()
