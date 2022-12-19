file = open("aoc15_input.txt")
l = file.read().split("\n")
file.close()

import heapq

class Unit:
    def __init__(self, id, x, y, side, health):
        self.id = id
        self.x = x
        self.y = y
        self.side = side
        self.health = health

w, h = len(l[0]), len(l)
g = [[0 for _ in range(w)] for _ in range(h)]

# id: (id, x, y, side, health)
units = {}

i = 1
alive = [0, 0]
for iy in range(h):
    for ix in range(w):
        if l[iy][ix] == "#":
            g[iy][ix] = -1
        elif l[iy][ix] in "GE":
            g[iy][ix] = i
            units[i] = Unit(i, ix, iy, l[iy][ix] == "E", 200)
            alive[l[iy][ix] == "E"] += 1
            i += 1

def get_closest_target(g, units, x, y, side):
    q = [(0, x, y)]
    visited = set()
    best = None

    while q:
        dist, x, y = heapq.heappop(q)

        if best and dist > best[0]:
            break
        
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for ix, iy in [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]:
            if g[iy][ix] == 0:
                heapq.heappush(q, (dist + 1, ix, iy))
            elif g[iy][ix] > 0:
                if units[g[iy][ix]].side != side:
                    if not best or y * w + x < best[2] * w + best[1]:
                        best = (dist, x, y)

    if best:
        return (best[1], best[2])
    else:
        return 0, 0

def get_distance_to(g, x, y, dx, dy):
    q = [(0, 0, x, y)]
    visited = set()

    while q:
        _, dist, x, y = heapq.heappop(q)

        if x == dx and y == dy:
            return dist
        
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for ix, iy in [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]:
            if g[iy][ix] == 0:
                heapq.heappush(q, (dist + 1 + abs(ix - dx) + abs(iy - dy), dist + 1, ix, iy))
    
    return 10**100

steps = 0
while alive[0] and alive[1]:
    steps += 1

    turns = []
    for iy in range(h):
        for ix in range(w):
            if g[iy][ix] > 0:
                turns.append(g[iy][ix])
    
    for i in turns:
        if i not in units.keys():
            continue

        u = units[i]
        x, y, side, health = u.x, u.y, u.side, u.health
        
        tx, ty = get_closest_target(g, units, x, y, side)
        
        if tx == 0:
            continue
        
        if tx != x or ty != y:
            best = (10**100, (x, y))
            for ix, iy in [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]:
                if g[iy][ix] == 0:
                    dist = get_distance_to(g, ix, iy, tx, ty)
                    if dist < best[0]:
                        best = (dist, ix, iy)
            
            u.x, u.y = best[1], best[2]
            g[y][x] = 0
            g[u.y][u.x] = i

            x, y = u.x, u.y
        
        best = None
        for ix, iy in [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]:
            if g[iy][ix] > 0:
                tu = units[g[iy][ix]]
                if tu.side != side:
                    if not best or tu.health < best.health:
                        best = tu
        
        if best:
            best.health -= 3
            if best.health <= 0:
                g[best.y][best.x] = 0
                alive[best.side] -= 1
                units.pop(best.id)

s = 0
for u in units.values():
    s += u.health
s *= steps - 1

print(s)