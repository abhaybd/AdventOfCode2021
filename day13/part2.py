def read_data(file):
    coords = set()
    folds = []
    with open(file) as f:
        line = f.readline()
        while line != "\n":
            coords.add(tuple(map(int, line.split(","))))
            line = f.readline()
        line = f.readline()
        while line:
            fold, val = line.split("=")
            axis = fold[-1]
            val = int(val)
            folds.append((axis, val))
            line = f.readline()
    return coords, folds

def fold_along_y(coords: set, y):
    for coord in list(filter(lambda c: c[1] > y, coords)):
        coords.remove(coord)
        new_coord = (coord[0], coord[1] - 2 * (coord[1] - y))
        coords.add(new_coord)

def fold_along_x(coords, x):
    for coord in list(filter(lambda c: c[0] > x, coords)):
        coords.remove(coord)
        new_coord = (coord[0] - 2 * (coord[0] - x), coord[1])
        coords.add(new_coord)

def print_grid(coords):
    max_x = max(map(lambda c: c[0], coords))
    max_y = max(map(lambda c: c[1], coords))
    for y in range(max_y+1):
        for x in range(max_x+1):
            print("#" if (x,y) in coords else ".", end="")
        print()

def main():
    coords, folds = read_data("input.txt")
    for axis, val in folds:
        if axis == "x":
            fold_along_x(coords, val)
        else:
            fold_along_y(coords, val)
    print_grid(coords)

if __name__ == "__main__":
    main()
