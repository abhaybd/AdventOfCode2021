def read_data():
    with open("input.txt") as f:
        lines = f.read().split("\n")
    vert_or_horiz_lines = []
    for line in lines:
        start, end = line.split(" -> ", 2)
        start_x, start_y = map(int, start.split(","))
        end_x, end_y = map(int, end.split(","))
        # filter by horizontal or vertical
        if start_x == end_x or start_y == end_y:
            # ensure increasing x
            if start_x < end_x:
                vert_or_horiz_lines.append(((start_x, start_y), (end_x, end_y)))
            elif start_x > end_x:
                vert_or_horiz_lines.append(((end_x, end_y), (start_x, start_y)))
            else:
                # ensure increasing y
                if start_y <= end_y:
                    vert_or_horiz_lines.append(((start_x, start_y), (end_x, end_y)))
                else:
                    vert_or_horiz_lines.append(((end_x, end_y), (start_x, start_y)))
    return vert_or_horiz_lines

# only works for vertical or horizontal lines
def point_in_line(x, y, p1, p2):
    if p1[0] == p2[0] == x and p1[1] <= y <= p2[1]:
        return True
    elif p1[1] == p2[1] == y and p1[0] <= x <= p2[0]:
        return True
    return False

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
        length = 1 + max(end[0] - start[0], abs(end[1] - start[1]))
        dx = 1 if end[0] > start[0] else 0
        dy = 1 if end[1] > start[1] else 0
        for i in range(length):
            x = start[0] + i * dx
            y = start[1] + i * dy
            if (x,y) not in visited:
                visited.add((x,y))
                if num_lines_at_point(lines, x, y) > 1:
                    ret += 1
    print(ret)

main()
