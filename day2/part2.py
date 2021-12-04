with open("input.txt") as f:
    lines = f.read().split("\n")

forward = 0
depth = 0
aim = 0
for line in lines:
    command, x = line.split(" ", 2)
    x = int(x)
    if command == "forward":
        forward += x
        depth += aim * x
    elif command == "down":
        aim += x
    elif command == "up":
        aim -= x

print(forward * depth)
