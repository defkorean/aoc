from pathlib import Path
import os
from shapely import Polygon

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILE = Path(SCRIPT_DIR, 'input.txt')

def parse_input():
    with open(INPUT_FILE, mode='rt') as f:
        data = f.read().splitlines()
        data = [tuple(int(x) for x in line.split(',')) for line in data]
        return data

def part1():
    coords = parse_input()
    
    max_area = 0
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            max_area = max(max_area, area(coords[i], coords[j]))
    return max_area

def area(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

def part2():
    coords = parse_input()
    polygon = Polygon(coords)
    max_area = 0

    for p1 in coords:
        for p2 in coords:
            min_x = min(p1[0], p2[0])
            min_y = min(p1[1], p2[1])
            max_x = max(p1[0], p2[0])
            max_y = max(p1[1], p2[1])
            cur_rect = Polygon(((min_x, min_y), (max_x, min_y), (max_x, max_y), (min_x, max_y)))
            if polygon.contains(cur_rect):  
                max_area = max(max_area, area(p1, p2))
    return max_area

print(part2())
