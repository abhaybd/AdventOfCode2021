def get_rating(data, majority, tiebreaker):
    idx = 0
    while len(data) > 1:
        occ = [0, 0]
        for line in data:
            occ[int(line[idx])] += 1
        if occ[0] > occ[1]:
            to_keep = "0" if majority else "1"
        elif occ[0] < occ[1]:
            to_keep = "1" if majority else "0"
        else:
            to_keep = tiebreaker
        data = [line for line in data if line[idx] == to_keep]
        idx += 1
    return data[0]

def main():
    with open("input.txt") as f:
        data = f.read().split("\n")

    oxygen = get_rating(data, True, "1")
    co2 = get_rating(data, False, "0")

    print(int(oxygen, 2) * int(co2, 2))

main()
