file = open("aoc23_input.txt")
g = file.read().split("\n")
file.close()

w, h = len(g[0]), len(g)

nodes = [(1, 0), (w - 2, h - 1)]
for iy in range(1, h - 1):
    for ix in range(1, w - 1):
        if g[iy][ix] == "#":
            continue

        c = 0
        for d in range(4):
            x = ix - (d == 0) + (d == 1)
            y = iy - (d == 2) + (d == 3)
            c += g[y][x] != "#"

        if c >= 3:
            nodes.append((ix, iy))

neighbors = {}
for a in nodes:
    x, y = a

    q = [(0, x, y, -1, -1)]

    while q:
        c, x, y, fx, fy = q.pop()

        b = (x, y)
        if b in nodes and a != b:
            neighbors[a] = neighbors.get(a, {})
            neighbors[a][b] = c
            continue

        for d in range(4):
            nx = x - (d == 0) + (d == 1)
            ny = y - (d == 2) + (d == 3)

            if nx < 0 or nx > w - 1 or ny < 0 or ny > h - 1:
                continue

            if g[ny][nx] == "#":
                continue
            if ny == fy and nx == fx:
                continue

            q.append((c + 1, nx, ny, x, y))

b = 0

q = [(0, 1, 0, 0)]
while q:
    c, x, y, seen = q.pop()

    if x == w - 2 and y == h - 1:
        if b < c:
            b = c
            print(f"{b} (?)")
        continue

    idx = nodes.index((x, y))
    seen |= 1 << idx

    for n, cost in neighbors[(x, y)].items():
        idx = nodes.index(n)
        if (seen >> idx) & 1:
            continue

        q.append((c + cost, n[0], n[1], seen))

print(b)