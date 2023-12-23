file = open("aoc23_input.txt")
g = file.read().split("\n")
file.close()

w, h = len(g[0]), len(g)

sx = 1
sy = 0

b = 0

q = [(0, sx, sy, -1, -1)]
while q:
    c, x, y, fx, fy = q.pop()

    if y == h - 1:
        b = max(b, c)
        continue

    for d in range(4):
        idx = "<>^v".find(g[y][x])
        if idx != -1 and d != idx:
            continue

        nx = x - (d == 0) + (d == 1)
        ny = y - (d == 2) + (d == 3)

        if g[ny][nx] == "#":
            continue
        if ny == fy and nx == fx:
            continue

        q.append((c + 1, nx, ny, x, y))

print(b)