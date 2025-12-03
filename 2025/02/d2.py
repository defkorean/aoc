from pathlib import Path
import os
import math 
import re

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILE = Path(SCRIPT_DIR, 'input.txt')

def parse_input():
    with open(INPUT_FILE, mode='rt') as f:
        data = f.read().split(',')
        return data

def part1():
    product_ids = parse_input()
    invalid_sum = 0
    for id in product_ids:
        first, last = id.split('-')
        for i in range(int(first), int(last) + 1):
            if (math.floor(math.log10(i)) + 1) % 2 == 0:
                check = str(i)
                half = len(check) // 2
                if check[:half] == check[half:]:
                    invalid_sum += i
    return invalid_sum


def part2():
    product_ids = parse_input()
    invalid_sum = 0
    for id in product_ids:
        first, last = id.split('-')
        for i in range(int(first), int(last) + 1):
            # regex that looks for start ^, group of one or more digits (\d+), look for same group that matches one or more times \1+, until the end of string $
            if re.match(r'^(\d+)\1+$', str(i)): 
                invalid_sum += i
    return invalid_sum

print(part2())
