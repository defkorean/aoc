from pathlib import Path
import os
from collections import defaultdict
import math

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILE = Path(SCRIPT_DIR, 'input.txt')

def parse_input():
    with open(INPUT_FILE, mode='rt') as f:
        data = [line for line in f] 
        return data

def part1():
    data = parse_input()
    digits = data[:len(data) - 1]
    operators = data[-1]

    grid = defaultdict(list)
    for d in digits:
        row = 0
        for c in d.split():
           grid[row].append(int(c))
           row += 1
    
    i = 0
    res = 0
    for o in operators.split():
        res += math.prod(grid[i]) if o == '*' else sum(grid[i])
        i += 1
    return res

def part2():
    data = parse_input()
    digits = data[:len(data) - 1]
    operators = data[-1]

    grid = defaultdict(list)
    for d in digits:
        for i, c in enumerate(d):
           if c not in' \n':
              grid[i].append(c)
    new_grid = {}
    for k, v in grid.items():
        new_grid[k] = int(''.join(grid[k]))
    
    res = 0
    stack = []
    for i in range(len(operators) - 1, -1, -1):
        if i in new_grid:
            stack.append(new_grid[i])
        if operators[i] in '*+':
            res += math.prod(stack) if operators[i] == '*' else sum(stack)
            stack = []
    return res

print(part2()) 
