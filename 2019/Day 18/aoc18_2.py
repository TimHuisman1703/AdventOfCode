file = open("aoc18_input.txt")
l = file.read().split("\n")
file.close()

import heapq

g = [[0 for _ in range(len(l[0]))] for _ in range(len(l))]

keys = {}

for iy in range(len(l)):
    for ix in range(len(l[0])):
        c = l[iy][ix]

        if c == "#":
            g[iy][ix] = 1
        elif c == "@":
            x, y = ix, iy
        elif c.isalpha():
            g[iy][ix] = ord(c)
            if c.islower():
                keys[c] = (ix, iy)

g[y-1][x-1], g[y-1][x], g[y-1][x+1] = 49, 1, 50
g[y][x-1], g[y][x], g[y][x+1] = 1, 1, 1
g[y+1][x-1], g[y+1][x], g[y+1][x+1] = 51, 1, 52

keys["1"] = (x - 1, y - 1)
keys["2"] = (x + 1, y - 1)
keys["3"] = (x - 1, y + 1)
keys["4"] = (x + 1, y + 1)

def distance(g, x, y, dx, dy):
    q = [(0, 0, x, y, "")]
    visited = set()

    while q:
        _, dist, x, y, required = heapq.heappop(q)

        if x == dx and y == dy:
            return (dist, required)

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for ix, iy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if g[iy][ix] == 1:
                continue
            
            c = chr(g[iy][ix])

            new_required = required
            if c.isupper() and c.lower():
                new_required = "".join(sorted(new_required + c.lower()))

            heapq.heappush(q, (dist + 1 + abs(ix - dx) + abs(iy - dy), dist + 1, ix, iy, new_required))

distances = {}
for i in keys.keys():
    for j in keys.keys():
        if i >= j:
            continue
        
        sx, sy = keys[i]
        dx, dy = keys[j]
        path = distance(g, sx, sy, dx, dy)
        if path:
            distances[(i, j)] = path
            distances[(j, i)] = path

q = [(0, "1234", ("1", "2", "3", "4"))]
visited = set()

while q:
    cost, unlocked, last = heapq.heappop(q)

    if (unlocked, last) in visited:
        continue
    visited.add((unlocked, last))

    if len(unlocked) == len(keys):
        print(cost)
        break
    
    for i in range(4):
        curr = last[i]
        for key in keys.keys():
            if key not in unlocked:
                if (curr, key) not in distances:
                    continue
                dist, required = distances[(curr, key)]
                for c in required:
                    if c not in unlocked:
                        break
                else:
                    new_last = tuple([last[j] if j != i else key for j in range(4)])
                    heapq.heappush(q, (cost + dist, "".join(sorted(unlocked + key)), new_last))