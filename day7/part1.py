from statistics import median

# main idea: median of array minimizes MAE of every element

def read_data():
    with open("input.txt") as f:
        crabs = list(map(int, f.read().split(",")))
    return crabs

def main():
    crabs = read_data()
    crabs.sort()
    align_pos = int(round(median(crabs)))
    total_cost = sum(abs(pos - align_pos) for pos in crabs)
    print(total_cost)

main()
