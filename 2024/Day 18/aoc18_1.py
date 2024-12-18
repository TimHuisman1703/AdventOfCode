file = open("aoc18_input.txt")
l = file.read().split("\n")
file.close()

import heapq

w = 71
h = 71

g = [[10 ** 10 for _ in range(w)] for _ in range(h)]
for i, s, in enumerate(l):
    x, y = [int(j) for j in s.split(",")]
    g[y][x] = i

q = [(0, 0, 0)]
visited = set()
while q:
    c, x, y = heapq.heappop(q)

    if g[y][x] <= 1023:
        continue

    if (x, y) in visited:
        continue
    visited.add((x, y))

    if x == w - 1 and y == h - 1:
        print(c)
        break

    for d in range(4):
        nx = x + (d == 0) - (d == 1)
        ny = y + (d == 2) - (d == 3)

        if nx < 0 or nx >= w or ny < 0 or ny >= h:
            continue

        heapq.heappush(q, (c + 1, nx, ny))