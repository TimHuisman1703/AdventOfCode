file = open("aoc03_input.txt")
g = file.read().split("\n")
file.close()

w, h = len(g[0]), len(g)

symbols = []
for iy in range(h):
    for ix in range(w):
        if not g[iy][ix].isdigit() and g[iy][ix] != ".":
            symbols.append((ix, iy))

s = 0
visited = [[False for _ in range(w)] for _ in range(h)]
for sym in symbols:
    q = [sym]
    starts = set()

    while q:
        x, y = q.pop()

        if g[y][x] == ".":
            continue

        if visited[y][x]:
            continue
        visited[y][x] = True

        if g[y][x].isdigit():
            starts.add((x, y))

        for iy in range(y - 1, y + 2):
            for ix in range(x - 1, x + 2):
                if ix < 0 or ix >= w or iy < 0 or iy >= h:
                    continue
                q.append((ix, iy))

    starts = {(x, y) for (x, y) in starts if (x - 1, y) not in starts}

    if len(starts) == 2:
        p = 1
        for x, y in starts:
            c = 0
            while x < w and g[y][x].isdigit():
                c = 10 * c + int(g[y][x])
                x += 1
            p *= c
        s += p

print(s)