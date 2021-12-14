def read_data(file):
    with open(file) as f:
        lines = f.read().split("\n")
    template = lines[0]
    rules = dict(map(lambda l: l.split(" -> "), lines[2:]))
    return template, rules

def do_insertion(polymer, rules):
    new_polymer = polymer[0]
    for i in range(len(polymer) - 1):
        pair = polymer[i:i+2]
        if pair in rules:
            new_polymer += rules[pair]
        new_polymer += polymer[i+1]
    return new_polymer

def build_char_map(s):
    charmap = {}
    for c in s:
        charmap[c] = charmap.get(c, 0) + 1
    return charmap

def main():
    polymer, rules = read_data("input.txt")
    for i in range(10):
        polymer = do_insertion(polymer, rules)

    charmap = build_char_map(polymer)
    print(max(charmap.values()) - min(charmap.values()))

if __name__ == "__main__":
    main()
