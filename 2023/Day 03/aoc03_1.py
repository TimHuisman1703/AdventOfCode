file = open("aoc03_input.txt")
g = file.read().split("\n")
file.close()

w, h = len(g[0]), len(g)

q = []
for iy in range(h):
    for ix in range(w):
        if not g[iy][ix].isdigit() and g[iy][ix] != ".":
            q.append((ix, iy))

visited = [[False for _ in range(w)] for _ in range(h)]
while q:
    x, y = q.pop()

    if g[y][x] == ".":
        continue

    if visited[y][x]:
        continue
    visited[y][x] = True

    for iy in range(y - 1, y + 2):
        for ix in range(x - 1, x + 2):
            if ix < 0 or ix >= w or iy < 0 or iy >= h:
                continue
            q.append((ix, iy))

s = 0
c = 0
for iy in range(h):
    for ix in range(w + 1):
        if ix < w and g[iy][ix].isdigit() and visited[iy][ix]:
            c = 10 * c + int(g[iy][ix])
        else:
            s += c
            c = 0

print(s)