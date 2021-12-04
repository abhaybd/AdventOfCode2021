with open("input.txt") as f:
    lines = f.read().split("\n")

forward = 0
depth = 0
for line in lines:
    command, x = line.split(" ", 2)
    x = int(x)
    if command == "forward":
        forward += x
    elif command == "down":
        depth += x
    elif command == "up":
        depth -= x

print(forward * depth)
