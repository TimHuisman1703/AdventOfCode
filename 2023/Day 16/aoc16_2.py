file = open("aoc16_input.txt")
g = file.read().split("\n")
file.close()

b = 0

for sy in range(len(g)):
    for sx in range(len(g[0])):
        for d in range(4):
            dx = (d == 0) - (d == 1)
            dy = (d == 2) - (d == 3)

            pos = False
            if sx == 0 and dx > 0:
                pos = True
            if sx == len(g[0]) - 1 and dx < 0:
                pos = True
            if sy == 0 and dy > 0:
                pos = True
            if sy == len(g) - 1 and dy < 0:
                pos = True
            if not pos:
                continue

            q = [(sx, sy, dx, dy)]
            ps = set()

            while q:
                nq = []
                for x, y, dx, dy in q:
                    if x < 0 or x >= len(g[0]) or y < 0 or y >= len(g):
                        continue

                    if (x, y, dx, dy) in ps:
                        continue
                    ps.add((x, y, dx, dy))

                    ds = []
                    if g[y][x] == "/":
                        ds.append((-dy, -dx))
                    elif g[y][x] == "\\":
                        ds.append((dy, dx))
                    elif g[y][x] == "-" and dx == 0:
                        ds.append((1, 0))
                        ds.append((-1, 0))
                    elif g[y][x] == "|" and dy == 0:
                        ds.append((0, 1))
                        ds.append((0, -1))
                    else:
                        ds.append((dx, dy))

                    nq.extend([(x + dx, y + dy, dx, dy) for dx, dy in ds])

                q = nq

            c = len(set([(x, y) for x, y, _, _ in ps]))
            b = max(b, c)

print(b)