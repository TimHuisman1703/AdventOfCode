file = open("aoc16_input.txt")
g = file.read().split("\n")
file.close()

import heapq

for iy in range(len(g)):
    for ix in range(len(g[0])):
        if g[iy][ix] == "S":
            sx, sy = ix, iy
        if g[iy][ix] == "E":
            ex, ey = ix, iy

q = [(0, sx, sy, 1, 0, None)]
visited = {}

r = set([(sx, sy), (ex, ey)])
best = -1

while q:
    cost, x, y, dx, dy, prev = heapq.heappop(q)

    if x == ex and y == ey:
        if best == -1:
            best = cost
        if cost > best:
            break

    key = (x, y, dx, dy)
    if key in visited:
        known_cost, known_pred = visited[key]
        if known_cost == cost:
            known_pred.add(prev)
        continue
    visited[key] = (cost, {prev})

    nx = x + dx
    ny = y + dy
    curr = (x, y, dx, dy)
    if g[ny][nx] != "#":
        heapq.heappush(q, (cost + 1, nx, ny, dx, dy, curr))
    heapq.heappush(q, (cost + 1000, x, y, dy, -dx, curr))
    heapq.heappush(q, (cost + 1000, x, y, -dy, dx, curr))

q = [(ex, ey, (d == 0) - (d == 1), (d == 2) - (d == 3)) for d in range(4)]
r = set([(ex, ey), (sx, sy)])
while q:
    curr = q.pop()
    if curr in visited:
        _, pred = visited[curr]
        q.extend(pred)
        if pred == {None}:
            continue
        r |= set([(x, y) for x, y, _, _ in pred])

print(len(r))