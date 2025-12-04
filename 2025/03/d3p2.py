from pathlib import Path
import os
import math 

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILE = Path(SCRIPT_DIR, 'input.txt')

def parse_input():
    with open(INPUT_FILE, mode='rt') as f:
        data = f.read().splitlines()
        return data

total_output = 0
for s in parse_input():
    batteries = []
    for window in range(12 - 1, -1, -1):
        # remove leftmost batteries after taking max of window
        i = s.index(max( s[:len(s) - window] ))
        batteries.append(s[i])
        s = s[i + 1:]

    total_output += int(''.join(batteries))

print(total_output)
