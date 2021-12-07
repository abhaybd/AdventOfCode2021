def read_data():
    with open("input.txt") as f:
        crabs = list(map(int, f.read().split(",")))
    return crabs

def move_cost(dist):
    return (dist**2 + dist) // 2

def total_cost(crabs, align_pos):
    return sum(move_cost(abs(pos - align_pos)) for pos in crabs)

def main():
    crabs = read_data()
    min_pos = min(crabs)
    max_pos = max(crabs)

    print(min(map(lambda p: total_cost(crabs, p), range(min_pos, max_pos + 1))))

main()
