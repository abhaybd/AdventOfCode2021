with open("input.txt") as f:
    lines = f.read().split("\n")

width = len(lines[0])

one_occ = [0] * width
for line in lines:
    for i, c in enumerate(line):
        if c == "1":
            one_occ[i] += 1

gamma = 0
thresh = len(lines) / 2
for n_occ in one_occ:
    gamma <<= 1
    if n_occ > thresh:
        gamma |= 1

epsilon = ~gamma & ((1 << width) - 1)

print(gamma * epsilon)
