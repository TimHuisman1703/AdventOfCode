file = open("aoc21_input.txt")
l = file.read().split("\n")
file.close()

import heapq

LAYERS = 2 + 23

pad = " ^A\n<V>".split("\n")

# > < V ^
dist = {(frc, toc): 1 for frc in "A><V^" for toc in "A><V^"}
positions = [(2, 0), (2, 1), (0, 1), (1, 1), (1, 0)]
for _ in range(LAYERS):
    dist_new = {}
    for fr in range(5):
        frc = "A><V^"[fr]
        for to in range(5):
            toc = "A><V^"[to]
            tox, toy = positions[to]

            if fr == to:
                dist_new[(frc, toc)] = 1
                continue

            q = [(0, *positions[fr], "A")]
            visited = set()
            while q:
                cost, x, y, p = heapq.heappop(q)

                key = (x, y, p)
                if key in visited:
                    continue
                visited.add(key)

                if x == tox and y == toy and p == "A":
                    dist_new[(frc, toc)] = cost
                    break

                for np in "A><V^":
                    nx = x + (np == ">") - (np == "<")
                    ny = y + (np == "V") - (np == "^")
                    if (nx, ny) not in positions:
                        continue
                    new_cost = cost + dist[(p, np)]
                    heapq.heappush(q, (new_cost, nx, ny, np))
    dist = dist_new

pad = "789\n456\n123\n 0A".split("\n")

r = 0
for w in l:
    q = [(0, 0, 2, 3, "A", None)]
    visited = set()
    while q:
        cost, idx, x, y, p, prev = heapq.heappop(q)

        key = (idx, x, y, p)
        if key in visited:
            continue
        visited.add(key)

        if idx == len(w):
            break
        elif pad[y][x] == w[idx]:
            np = "A"
            new_cost = cost + dist[(p, np)]
            heapq.heappush(q, (new_cost, idx + 1, x, y, np, key))
            continue

        for d in range(4):
            nx = x + (d == 0) - (d == 1)
            ny = y + (d == 2) - (d == 3)
            if nx < 0 or nx >= len(pad[0]) or ny < 0 or ny >= len(pad):
                continue
            if pad[ny][nx] == " ":
                continue

            np = "><V^"[d]
            new_cost = cost + dist[(p, np)]
            heapq.heappush(q, (new_cost, idx, nx, ny, np, key))

    w = w[:-1]
    while w[0] == "0":
        w = w[1:]
    r += cost * int(w)

print(r)
