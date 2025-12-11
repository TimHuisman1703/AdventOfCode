file = open("aoc10_input.txt")
l = file.read().split("\n")
file.close()

import heapq

r = 0
for row in l:
    t, *ps, _ = row.split()

    t = tuple(int(v == "#") for v in t[1:-1])
    ps = [tuple([int(j) for j in p[1:-1].split(",")]) for p in ps]

    q = [(0, t)]
    visited = set()
    while q:
        c, cur = heapq.heappop(q)

        if not any(cur):
            r += c
            break
        
        if cur in visited:
            continue
        visited.add(cur)

        for p in ps:
            nxt = tuple([cur[j] ^ (j in p) for j in range(len(cur))])
            heapq.heappush(q, (c + 1, nxt))

print(r)