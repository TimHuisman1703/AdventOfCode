file = open("aoc10_input.txt")
l = file.read().split("\n")
file.close()

visited = [[False for _ in range(len(l[0]))] for _ in range(len(l))]

for sy in range(len(l)):
    for sx in range(len(l[0])):
        if l[sy][sx] == "S":
            for d in range(4):
                q = [(
                    sx + (d == 0) - (d == 1),
                    sy + (d == 2) - (d == 3),
                    None
                )]
                locs = set([(sx, sy)])
                pos = True

                while q:
                    x, y, prev = q.pop()

                    if y < 0 or y >= len(l) or x < 0 or x >= len(l[0]) or l[y][x] == ".":
                        pos = False
                        break

                    if visited[y][x]:
                        continue
                    visited[y][x] = True
                    locs.add((x, y))

                    next = []
                    if l[y][x] == "-":
                        next = [(x - 1, y), (x + 1, y)]
                    if l[y][x] == "|":
                        next = [(x, y - 1), (x, y + 1)]
                    if l[y][x] == "L":
                        next = [(x, y - 1), (x + 1, y)]
                    if l[y][x] == "F":
                        next = [(x, y + 1), (x + 1, y)]
                    if l[y][x] == "7":
                        next = [(x, y + 1), (x - 1, y)]
                    if l[y][x] == "J":
                        next = [(x, y - 1), (x - 1, y)]
                    if l[y][x] == "S":
                        continue

                    if prev != None and prev not in next:
                        pos = False
                        break

                    q.extend([(*j, (x, y)) for j in next if j != prev])

                result = len(locs) // 2
                if pos and result:
                    g = [[False for _ in range(len(l[0]) * 2 + 1)] for _ in range(len(l) * 2 + 1)]
                    for x, y in locs:
                        gx = 2 * x + 1
                        gy = 2 * y + 1
                        g[gy][gx] = True
                        if l[y][x] == "-":
                            g[gy][gx - 1] = True
                            g[gy][gx + 1] = True
                        if l[y][x] == "|":
                            g[gy - 1][gx] = True
                            g[gy + 1][gx] = True
                        if l[y][x] == "L":
                            g[gy][gx + 1] = True
                            g[gy - 1][gx] = True
                        if l[y][x] == "F":
                            g[gy][gx + 1] = True
                            g[gy + 1][gx] = True
                        if l[y][x] == "7":
                            g[gy][gx - 1] = True
                            g[gy + 1][gx] = True
                        if l[y][x] == "J":
                            g[gy][gx - 1] = True
                            g[gy - 1][gx] = True

                    enclosed = 0
                    filled = [[False for _ in range(len(g[0]))] for _ in range(len(g))]
                    for iy in range(len(g)):
                        for ix in range(len(g[0])):
                            if not g[iy][ix] and not filled[iy][ix]:
                                q = [(ix, iy)]
                                pos = True
                                filled_now = 0

                                while q:
                                    x, y = q.pop()

                                    if y < 0 or y >= len(g) or x < 0 or x >= len(g[0]):
                                        pos = False
                                        continue

                                    if g[y][x]:
                                        continue

                                    if filled[y][x]:
                                        continue
                                    filled[y][x] = True
                                    filled_now += (x % 2) * (y % 2)

                                    for d in range(4):
                                        q.append((
                                            x + (d == 0) - (d == 1),
                                            y + (d == 2) - (d == 3)
                                        ))

                                if pos:
                                    enclosed += filled_now

                    print(enclosed)
