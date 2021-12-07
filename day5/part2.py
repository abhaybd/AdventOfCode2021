import math

def read_data():
    with open("input.txt") as f:
        lines_str = f.read().split("\n")
    lines = []
    for line in lines_str:
        start, end = line.split(" -> ", 2)
        start = tuple(int(x) for x in start.split(","))
        end = tuple(int(x) for x in end.split(","))
        if start[0] < end[0]:
            lines.append((start, end))
        elif start[0] > end[0]:
            lines.append((end, start))
        else:
            if start[1] <= end[1]:
                lines.append((start, end))
            else:
                lines.append((end, start))
    return lines

def norm_diff(p1, p2):
    if p1 == p2:
        return 0, 0
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    if dx != 0:
        dx = math.copysign(1, dx)
    if dy != 0:
        dy = math.copysign(1, dy)
    return dx, dy

def point_in_line(x, y, p1, p2):
    if (x,y) == p1 or (x,y) == p2:
        return True
    elif p1[0] == p2[0] == x: # horizontal case
        return p1[1] <= y <= p2[1]
    elif p1[1] == p2[1] == y: # vertical case
        return p1[0] <= x <= p2[0]
    elif (abs(x-p1[0]) == abs(y-p1[1])) and (abs(x-p2[0]) == abs(y - p2[1])): # diagonal case
        return norm_diff(p1, (x,y)) == norm_diff((x,y), p2)

def num_lines_at_point(lines, x, y):
    ret = 0
    for line in lines:
        if point_in_line(x, y, *line):
            ret += 1
    return ret

def main():
    lines = read_data()
    ret = 0
    visited = set()
    for (start, end) in lines:
        dx, dy = norm_diff(start, end)
        length = 1 + max(end[0] - start[0], abs(end[1] - start[1]))
        for i in range(length):
            x = start[0] + i * dx
            y = start[1] + i * dy
            if (x,y) not in visited:
                visited.add((x,y))
                if num_lines_at_point(lines, x, y) > 1:
                    ret += 1
    print(ret)

main()
