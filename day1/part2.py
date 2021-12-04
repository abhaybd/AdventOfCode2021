with open("input.txt") as f:
    data = [int(s) for s in f.read().split("\n")]

num_increases = 0
prev = None
for i in range(len(data)-2):
    window_sum = sum(data[i:i+3])
    if prev is not None and window_sum > prev:
        num_increases += 1
    prev = window_sum

print(num_increases)
