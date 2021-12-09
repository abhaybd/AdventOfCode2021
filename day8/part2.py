from typing import List, Set

original_segment_map = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9
}

NUM_SEGMENTS = {v: len(k) for k, v in original_segment_map.items()}

def read_data(file):
    with open(file) as f:
        lines = f.read().split("\n")
    patterns = []
    codes = []
    for line in lines:
        pattern, code = line.split(" | ")
        patterns.append(list(map(set, pattern.split(" "))))
        codes.append(code.split(" "))
    return patterns, codes

def invert_dict(d: dict):
    return {v: k for k, v in d.items()}

def get_mapping(patterns: List[Set[str]]):
    # original to new segment map, key/val from "abcdefg"
    segment_map = {}

    one = next(p for p in patterns if len(p) == NUM_SEGMENTS[1])
    four = next(p for p in patterns if len(p) == NUM_SEGMENTS[4])
    seven = next(p for p in patterns if len(p) == NUM_SEGMENTS[7])
    eight = next(p for p in patterns if len(p) == NUM_SEGMENTS[8])

    segment_map['a'] = seven.difference(one).pop()

    eg = eight.difference(four).difference(segment_map['a'])
    nine = next(p for p in patterns if len(p) == 6 and not eg.issubset(p))
    segment_map['e'] = eight.difference(nine).pop()
    segment_map['g'] = nine.difference(four).difference(segment_map['a']).pop()

    zero_six = [p for p in patterns if len(p) == 6 and p is not nine]
    assert(len(zero_six) == 2)
    cd = zero_six[0].symmetric_difference(zero_six[1])
    segment_map['c'] = next(seg for seg in cd if seg in one)
    segment_map['d'] = cd.difference(segment_map['c']).pop()

    segment_map['f'] = seven.difference(segment_map['a']).difference(segment_map['c']).pop()
    segment_map['b'] = eight.difference(segment_map.values()).pop()

    return invert_dict(segment_map)

def decode(patterns, codes):
    segment_map = get_mapping(patterns)
    decoded_code = ""
    for code in codes:
        mapped_code = "".join(sorted(map(lambda c: segment_map[c], code)))
        decoded_code += str(original_segment_map[mapped_code])
    return int(decoded_code)


def main():
    out_sum = sum(decode(patterns, codes) for patterns, codes in zip(*read_data("input.txt")))
    print(out_sum)

main()
