file = open("aoc21_input.txt")
l = file.read().split("\n")
file.close()

import heapq

pads = [j.split("\n") for j in ["789\n456\n123\n 0A", " ^A\n<V>"]]

ds = [{}, {}]
for i, p in enumerate(pads):
    for iy in range(len(p)):
        for ix in range(len(p[0])):
            ds[i][p[iy][ix]] = (ix, iy)
pad0, pad1 = pads

r = 0
for w in l:
    d0, d1 = ds

    q = [(0, 0, *d0["A"], *d1["A"], *d1["A"], None)]
    visited = {}
    while q:
        cost, idx, ax, ay, bx, by, cx, cy, prev = heapq.heappop(q)

        key = (idx, ax, ay, bx, by, cx, cy)
        if key in visited:
            continue
        visited[key] = (cost, prev)

        if idx == len(w):
            break

        for d in range(4):
            nbx = bx + (d == 0) - (d == 1)
            nby = by + (d == 2) - (d == 3)
            if nbx < 0 or nbx >= len(pad1[0]) or nby < 0 or nby >= len(pad1):
                continue
            if pad1[nby][nbx] == " ":
                continue

            ncx, ncy = d1["><V^"[d]]
            new_cost = cost + abs(cx - ncx) + abs(cy - ncy) + 1
            heapq.heappush(q, (new_cost, idx, ax, ay, nbx, nby, ncx, ncy, key))

        for d in range(4):
            if pad1[by][bx] != "><V^"[d]:
                continue
            nax = ax + (d == 0) - (d == 1)
            nay = ay + (d == 2) - (d == 3)
            if nax < 0 or nax >= len(pad0[0]) or nay < 0 or nay >= len(pad0):
                continue
            if pad0[nay][nax] == " ":
                continue
            ncx, ncy = d1["A"]
            new_cost = cost + abs(cx - ncx) + abs(cy - ncy) + 1
            heapq.heappush(q, (new_cost, idx, nax, nay, bx, by, ncx, ncy, key))

        if pad1[by][bx] == "A":
            if pad0[ay][ax] == w[idx]:
                ncx, ncy = d1["A"]
                new_cost = cost + abs(cx - ncx) + abs(cy - ncy) + 1
                heapq.heappush(q, (new_cost, idx + 1, ax, ay, bx, by, ncx, ncy, key))

    w = w[:-1]
    while w[0] == "0":
        w = w[1:]
    r += cost * int(w)

print(r)