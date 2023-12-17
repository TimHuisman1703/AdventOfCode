file = open("aoc16_input.txt")
g = file.read().split("\n")
file.close()

ps = set()

x = y = 0
dx = 1
dy = 0

q = [(0, 0, 0, 1)]
while q:
    nq = []
    for x, y, dx, dy in q:
        if (x, y, dx, dy) in ps:
            continue
        ps.add((x, y, dx, dy))

        x += dx
        y += dy

        if x < 0 or x >= len(g[0]) or y < 0 or y >= len(g):
            continue

        if g[y][x] == "/":
            nq.append((x, y, -dy, -dx))
        elif g[y][x] == "\\":
            nq.append((x, y, dy, dx))
        elif g[y][x] == "-" and dx == 0:
            nq.append((x, y, 1, 0))
            nq.append((x, y, -1, 0))
        elif g[y][x] == "|" and dy == 0:
            nq.append((x, y, 0, 1))
            nq.append((x, y, 0, -1))
        elif g[y][x] == "-" or g[y][x] == "|":
            nq.append((x, y, dx, dy))
        elif g[y][x] == ".":
            nq.append((x, y, dx, dy))

    q = nq

print(len(set([(x, y) for x, y, _, _ in ps])))