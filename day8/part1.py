NUM_SEGMENTS = {
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

def read_data(file):
    with open(file) as f:
        lines = f.read().split("\n")
    patterns = []
    codes = []
    for line in lines:
        pattern, code = line.split(" | ")
        patterns.append(pattern.split(" "))
        codes.append(code.split(" "))
    return patterns, codes

def main():
    _, codes = read_data("input.txt")
    n_ones = sum(sum(len(p) == NUM_SEGMENTS[1] for p in pattern) for pattern in codes)
    n_fours = sum(sum(len(p) == NUM_SEGMENTS[4] for p in pattern) for pattern in codes)
    n_sevens = sum(sum(len(p) == NUM_SEGMENTS[7] for p in pattern) for pattern in codes)
    n_eights = sum(sum(len(p) == NUM_SEGMENTS[8] for p in pattern) for pattern in codes)
    print(n_ones + n_fours + n_sevens + n_eights)

main()