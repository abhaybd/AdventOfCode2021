with open("input.txt") as f:
    data = [int(s) for s in f.read().split("\n")]

num_increases = 0
for i in range(1, len(data)):
    if data[i] > data[i-1]:
        num_increases += 1

print(num_increases)
