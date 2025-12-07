file = open("aoc07_input.txt")
g = file.read().split("\n")
file.close()

import heapq

x = g[0].find("S")
y = 0

q = [(y, x, 1)]
r = 0

while q:
    y, x, c = heapq.heappop(q)

    while q and q[0][0] == y and q[0][1] == x:
        y, x, nc = heapq.heappop(q)
        c += nc

    ny = y + 1
    if ny >= len(g):
        continue

    if g[ny][x] == "^":
        r += 1
        heapq.heappush(q, (ny, x - 1, c))
        heapq.heappush(q, (ny, x + 1, c))
    else:
        heapq.heappush(q, (ny, x, c))

print(r)