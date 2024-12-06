file = open("aoc06_input.txt")
l = file.read().split("\n")
file.close()

g = [[x == "#" for x in row] for row in l]

for iy in range(len(g)):
    for ix in range(len(g[0])):
        if l[iy][ix] == "^":
            sx = ix
            sy = iy

r = 0

for by in range(len(g)):
    print(f"{by=}")
    for bx in range(len(g[0])):
        if g[by][bx]:
            continue
        g[by][bx] = True

        seen = set()
        dx = 0
        dy = -1
        x, y = sx, sy
        while True:
            if (x, y, dx, dy) in seen:
                r += 1
                break
            seen.add((x, y, dx, dy))

            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= len(g[0]) or ny < 0 or ny >= len(g):
                break

            if g[ny][nx]:
                dx, dy = -dy, dx
                continue

            x, y = nx, ny

        g[by][bx] = False

print(r)