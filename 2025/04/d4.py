from pathlib import Path
import os

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILE = Path(SCRIPT_DIR, 'input.txt')

def parse_input():
    with open(INPUT_FILE, mode='rt') as f:
        data = [list(x.strip('\n')) for x in f.readlines()]
        return data

def part1():
    grid = parse_input()
    m, n = len(grid), len(grid[0])
    total_rolls = 0

    for r in range(m):
        for c in range(n):
            if grid[r][c] == '@':
                if paper_rolls(m, n, grid, r, c) < 4:
                    total_rolls += 1
    return total_rolls


def paper_rolls(m, n, grid, cur_r, cur_c) -> int:
    rolls = 0
    adjacent = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, -1], [1, 1], [-1, 1], [-1, -1]]
    
    for r, c in adjacent:
        dr, dc = r + cur_r, c + cur_c
        if dr in range(m) and dc in range(n) and grid[dr][dc] == '@':
            rolls += 1

    return rolls 

# print(part1())

def part2():
    grid = parse_input()
    m, n = len(grid), len(grid[0])
    total_rolls = 0
    while True: 
        to_remove = []
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '@':
                    if paper_rolls(m, n, grid, r, c) < 4:
                        total_rolls += 1
                        to_remove.append((r, c))

        if len(to_remove) == 0:
            break
        for r, c in to_remove:
            grid[r][c] = '.'

    return total_rolls

print(part2())
