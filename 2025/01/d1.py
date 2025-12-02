from pathlib import Path
import os

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILE = Path(SCRIPT_DIR, 'input.txt')

def parse_input():
    with open(INPUT_FILE, mode='rt') as f:
        data = f.read().splitlines()
        return data

def part1():
    document = parse_input() 
    
    cur = 50
    res = 0

    for rotation in document:
        dir, change = rotation[0], int(rotation[1:])
        
        # convert left to right to make math simpler for next line
        if dir == 'L':
            change = 100 - change
        cur = (cur + change) % 100
        if cur == 0:
            res += 1
    return res
    

print(part1())

def part2():
    document = parse_input()

    cur = 50
    res = 0

    for rotation in document:
        dir, change = rotation[0], int(rotation[1:])
        
        for _ in range(change):

            if dir == 'R':
                cur = (cur + 1) % 100
            else:
                cur = (cur - 1) % 100

            if cur == 0:
                res += 1
    return res

print(part2())
