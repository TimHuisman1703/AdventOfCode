file = open("aoc20_input.txt")
g = [list(row) for row in file.read().split("\n")]
file.close()

SIZE = 20
GAIN = 100

import heapq

for iy in range(len(g)):
    for ix in range(len(g[0])):
        if g[iy][ix] == "S":
            sx, sy = ix, iy
        if g[iy][ix] == "E":
            ex, ey = ix, iy

q = [(0, sx, sy)]
ds = [[10 ** 10 for _ in range(len(g[0]))] for _ in range(len(g))]
normal_cost = 0
while q:
    cost, x, y = heapq.heappop(q)

    key = (x, y)
    if ds[y][x] < 10 ** 10:
        continue
    ds[y][x] = cost

    if (x, y) == (ex, ey):
        normal_cost = cost

    for d in range(4):
        nx = x + (d == 0) - (d == 1)
        ny = y + (d == 2) - (d == 3)
        if g[ny][nx] != "#":
            heapq.heappush(q, (cost + 1, nx, ny))

q = [(0, ex, ey)]
de = [[10 ** 10 for _ in range(len(g[0]))] for _ in range(len(g))]
while q:
    cost, x, y = heapq.heappop(q)

    key = (x, y)
    if de[y][x] < 10 ** 10:
        continue
    de[y][x] = cost

    for d in range(4):
        nx = x + (d == 0) - (d == 1)
        ny = y + (d == 2) - (d == 3)
        if g[ny][nx] != "#":
            heapq.heappush(q, (cost + 1, nx, ny))

r = 0
test = {}
for iy in range(len(g)):
    print(f"{iy=}")
    for ix in range(len(g[0])):
        if g[iy][ix] != "#":
            for dy in range(-SIZE, SIZE + 1):
                for dx in range(-SIZE, SIZE + 1):
                    dist = abs(dx) + abs(dy)
                    if dist > SIZE:
                        continue

                    jx, jy = ix + dx, iy + dy
                    if jx < 0 or jx >= len(g[0]) or jy < 0 or jy >= len(g):
                        continue

                    cost = ds[iy][ix] + dist + de[jy][jx]
                    gain = normal_cost - cost
                    if gain >= GAIN:
                        test[gain] = test.get(gain, 0) + 1
                        r += 1

print(r)