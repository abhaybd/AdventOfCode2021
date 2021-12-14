def read_data(file):
    with open(file) as f:
        lines = f.read().split("\n")
    template = lines[0]
    polymer_pairs = {}
    for i in range(len(template) - 1):
        pair = template[i:i+2]
        polymer_pairs[pair] = polymer_pairs.get(pair, 0) + 1
    rules = dict(map(lambda l: l.split(" -> "), lines[2:]))
    return template, polymer_pairs, rules

def do_insertion(polymer_pairs, rules):
    new_pairs = {}
    for pair, count in polymer_pairs.items():
        if pair in rules:
            insertion = rules[pair]
            first = pair[0] + insertion
            second = insertion + pair[1]
            new_pairs[first] = new_pairs.get(first, 0) + count
            new_pairs[second] = new_pairs.get(second, 0) + count
        else:
            new_pairs[pair] = new_pairs.get(pair, 0) + count
    return new_pairs

def build_charmap(template, pairs):
    charmap = {}
    for pair, count in pairs.items():
        for c in pair:
            charmap[c] = charmap.get(c, 0) + count
    # correct for overcounting
    for c, count in charmap.items():
        charmap[c] = count // 2
    # add first and last chars aren't overcounted
    charmap[template[0]] += 1
    charmap[template[-1]] += 1
    return charmap

def main():
    template, polymer_pairs, rules = read_data("input.txt")
    for i in range(40):
        polymer_pairs = do_insertion(polymer_pairs, rules)

    charmap = build_charmap(template, polymer_pairs)
    print(max(charmap.values()) - min(charmap.values()))


if __name__ == "__main__":
    main()
