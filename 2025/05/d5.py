from pathlib import Path
import os

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILE = Path(SCRIPT_DIR, 'input.txt')

def parse_input():
    with open(INPUT_FILE, mode='rt') as f:
        data = f.read().splitlines()
        fresh_ranges = []
        idx = 0
        for i, d in enumerate(data):
            if d == '':
                idx = i
                break
            s, e = d.split('-')
            fresh_ranges.append((int(s), int(e)))
        ingredients = []
        for i in range(idx + 1, len(data)):
            ingredients.append(int(data[i]))
        return (fresh_ranges, ingredients)

def part1():
    fresh_ranges, ingredients = parse_input()
    fresh_ranges.sort(key=lambda x: x[0])
    num_fresh = 0
    for i in ingredients:
        for s, e in fresh_ranges:
            if i >= s and i <= e:
                num_fresh += 1
                break
    return num_fresh

# just a leetcode problem, merge intervals specifically with some quick maths
def part2():
    fresh_ranges, _ = parse_input()
    fresh_ranges.sort(key=lambda x: x[0])
    reduced_range = [fresh_ranges[0]]
    for s, e in fresh_ranges[1:]:
        if reduced_range[-1][1] >= s:
            reduced_range[-1] = (reduced_range[-1][0], max(reduced_range[-1][1], e))
        else:
            reduced_range.append((s, e))
    return sum(e - s + 1 for s, e in reduced_range)
print(part2())
