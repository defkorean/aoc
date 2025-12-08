from pathlib import Path
import os
from collections import defaultdict

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILE = Path(SCRIPT_DIR, 'input.txt')

def parse_input():
    with open(INPUT_FILE, mode='rt') as f:
        data = f.read().splitlines()
        return data

def solution():
    manifold = parse_input()
    
    num_splits = 0
    beams = {manifold.pop(0).index('S') : 1}
    manifold = [line for line in manifold if '^' in line]
    
    for r in manifold:
        next_beams = defaultdict(int)
        
        for i, n in beams.items():
            if r[i] == '^':
                num_splits += 1
                next_beams[i - 1] += n
                next_beams[i + 1] += n
            else:
                next_beams[i] += n

        beams = next_beams
    return num_splits, sum(beams[i] for i in beams)
print(solution())
