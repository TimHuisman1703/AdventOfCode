file = open("aoc12_input.txt")
g = file.read().split("\n")
file.close()

from collections import deque

sx = sy = 0
ex = ey = 0
for iy in range(len(g)):
    for ix in range(len(g[0])):
        if g[iy][ix] == "S":
            sx, sy = ix, iy
        elif g[iy][ix] == "E":
            ex, ey = ix, iy
    g[iy] = g[iy].replace("S", "a").replace("E", "z")

q = deque()
q.append((0, sx, sy))
v = set()

while q:
    c, x, y = q.popleft()

    if x == ex and y == ey:
        print(c)
        break

    if (x, y) in v:
        continue
    v.add((x, y))

    for i in range(4):
        ix, iy = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)][i]

        if iy < 0 or iy >= len(g) or ix < 0 or ix >= len(g[0]):
            continue
        
        if ord(g[iy][ix]) - ord(g[y][x]) > 1:
            continue
        
        q.append((c + 1, ix, iy))