file = open("aoc24_input.txt")
g = file.read().split("\n")
file.close()

from collections import deque

b = []
for iy in range(len(g)):
    for ix in range(len(g[iy])):
        if g[iy][ix] in ">v<^":
            b.append((ix, iy, ">v<^".index(g[iy][ix])))

height, width = len(g), len(g[0])

total = 0
for stage in range(3):
    gx, gy = [(width - 2, height - 1), (1, 0)][stage % 2]
    sx, sy = [(width - 2, height - 1), (1, 0)][1 - stage % 2]
    q = deque([(0, sx, sy)])
    visited = set()
    prev_cost = 0
    blocked = set()

    while q:
        cost, x, y = q.popleft()

        if prev_cost < cost:
            visited = set()
            nb = []
            blocked = set()
            for bx, by, bd in b:
                nx = (bx + (bd == 0) - (bd == 2) - 1) % (width - 2) + 1
                ny = (by + (bd == 1) - (bd == 3) - 1) % (height - 2) + 1
                nb.append((nx, ny, bd))
                blocked.add((nx, ny))
            b = nb
            prev_cost = cost

        if x == gx and y == gy:
            total += cost
            break

        key = (x, y)
        if key in visited:
            continue
        visited.add(key)

        if key in blocked:
            continue

        for i in range(5):
            nx = x + (i == 0) - (i == 2)
            ny = y + (i == 1) - (i == 3)
            if nx > 0 and nx < width - 1 and (ny > 0 or nx == 1) and (ny < height - 1 or nx == width - 2):
                q.append((cost + 1, nx, ny))

print(total)