file = open("aoc20_input.txt")
g = [list(row) for row in file.read().split("\n")]
file.close()

import heapq

for iy in range(len(g)):
    for ix in range(len(g[0])):
        if g[iy][ix] == "S":
            sx, sy = ix, iy
        if g[iy][ix] == "E":
            ex, ey = ix, iy

normal_cost = 0
    
q = [(0, sx, sy)]
visited = set()
while q:
    cost, x, y = heapq.heappop(q)

    if x == ex and y == ey:
        normal_cost = cost
        break

    key = (x, y)
    if key in visited:
        continue
    visited.add(key)

    for d in range(4):
        nx = x + (d == 0) - (d == 1)
        ny = y + (d == 2) - (d == 3)
        if g[ny][nx] != "#":
            heapq.heappush(q, (cost + 1, nx, ny))

r = 0
for by in range(1, len(g) - 1):
    print(f"{by=}")
    for bx in range(1, len(g[0]) - 1):
        if g[by][bx] == "#":
            g[by][bx] = "."
    
            q = [(0, sx, sy)]
            visited = set()
            while q:
                cost, x, y = heapq.heappop(q)

                if x == ex and y == ey:
                    if cost + 100 <= normal_cost:
                        r += 1
                    break

                key = (x, y)
                if key in visited:
                    continue
                visited.add(key)

                for d in range(4):
                    nx = x + (d == 0) - (d == 1)
                    ny = y + (d == 2) - (d == 3)
                    if g[ny][nx] != "#":
                        heapq.heappush(q, (cost + 1, nx, ny))
            
            g[by][bx] = "#"

print(r)