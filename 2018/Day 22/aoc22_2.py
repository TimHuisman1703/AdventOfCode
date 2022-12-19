file = open("aoc22_input.txt")
l = file.read().split("\n")
file.close()

import heapq

depth = int(l[0].split()[-1])
tx, ty = [int(j) for j in l[1].split()[-1].split(",")]

mem = {}

def erosion_level(x, y):
    global mem

    key = (x, y)
    if key in mem.keys():
        return mem[key]
    
    if y == 0:
        geo = x * 16807
    elif x == 0:
        geo = y * 48271
    elif x == tx and y == ty:
        geo = 0
    else:
        geo = erosion_level(x - 1, y) * erosion_level(x, y - 1)
    
    mem[key] = (geo + depth) % 20183
    return mem[key]

# 0: nothing, 1: torch, 2: climbing gear
q = [(0, 0, 0, 0, 1)]
visited = set()

while 1:
    _, time, x, y, equiped = heapq.heappop(q)

    if (x, y, equiped) in visited:
        continue
    visited.add((x, y, equiped))

    if x == tx and y == ty and equiped == 1:
        print(time)
        break
    
    heapq.heappush(q, (time + 7 + abs(x - tx) + abs(y - ty), time + 7, x, y, (3 - equiped - erosion_level(x, y)) % 3))
    for ix, iy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if ix < 0 or iy < 0:
            continue
        
        if erosion_level(ix, iy) % 3 != equiped:
            heapq.heappush(q, (time + 1 + abs(ix - tx) + abs(iy - ty), time + 1, ix, iy, equiped))