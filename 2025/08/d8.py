from pathlib import Path
import os
import heapq
from math import sqrt, pow

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILE = Path(SCRIPT_DIR, 'input.txt')

def parse_input():
    with open(INPUT_FILE, mode='rt') as f:
        data = f.read().splitlines()
        return data

class UF:
    def __init__(self, n):
        self.parent = {}
        for id in range(n):
            self.parent[id] = id

    def find(self, v):
        if self.parent[v] == v:
            return v
        return self.find(self.parent[v])

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)

        if i != j:
            self.parent[i] = j

def solutions():
    boxes = parse_input()
    boxes = [[int(x) for x in box.split(',')] for box in boxes]
    pq = []
    heapq.heapify(pq)
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            if boxes[i] != boxes[j]:
                x1, y1, z1 = boxes[i]
                x2, y2, z2 = boxes[j]
                dist = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2) + pow(z1 - z2, 2)) 
                heapq.heappush(pq, (dist, i, j))

    uf = UF(len(boxes))
    i = 0
    p1, p2 = 0, 0
    while i < 1000:
       _, u, v = heapq.heappop(pq)
       uf.union(u, v)
       i += 1          
    parents = {i : 0 for i in range(len(boxes))}
    for i in range(len(boxes)):
        j = uf.find(i)
        parents[j] += 1
    k = sorted(parents.values())
    p1 = k[-3] * k[-2] * k[-1]

    while pq:
        _, u, v = heapq.heappop(pq)
        uf.union(u, v)
        if all(uf.find(u) == uf.find(0) for u in range(len(boxes))):
            p2 = boxes[u][0] * boxes[v][0]
            break
    
    return p1, p2
print(solutions())

