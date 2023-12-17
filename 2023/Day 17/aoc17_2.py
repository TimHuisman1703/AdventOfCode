file = open("aoc17_input.txt")
g = file.read().split("\n")
file.close()

import heapq

g = [[int(j) for j in row] for row in g]

q = [(0, 0, 0, 1, 0)]
seen = set()
while q:
    cost, x, y, dir, mult = heapq.heappop(q)

    key = (x, y, dir, mult)
    if key in seen:
        continue
    seen.add(key)

    if x == len(g[0]) - 1 and y == len(g) - 1:
        print(cost)
        break

    for d in range(4):
        if d != dir and mult < 4:
            continue
        if d == dir and mult == 10:
            continue

        if d != dir and d // 2 == dir // 2:
            continue

        nx = x - (d == 0) + (d == 1)
        ny = y - (d == 2) + (d == 3)

        if nx < 0 or nx >= len(g[0]) or ny < 0 or ny >= len(g):
            continue

        heapq.heappush(q, (cost + g[ny][nx], nx, ny, d, mult * (d == dir) + 1))