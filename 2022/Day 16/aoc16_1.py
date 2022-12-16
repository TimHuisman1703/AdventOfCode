file = open("aoc16_input.txt")
l = file.read().split("\n")
file.close()

import heapq

rate = {}
neighbors = {}

for i in l:
    i = i.split()
    name = i[1]
    rate[name] = int(i[4][5:-1])
    neighbors[name] = [j[:2] for j in i[9:]]

q = [((-30, 0), 30, 0, 0, "AA", set(), "-")]
v = set()

m = 30

while q:
    _, left, pressure, curr_rate, pos, done, came_from = heapq.heappop(q)

    if left < m:
        v = set()
        m = left
        print(m, pressure, len(q))

        if left == 0:
            print(pressure)
            break

    key = (pos, curr_rate)
    if key in v:
        continue
    v.add(key)

    pressure += curr_rate

    if rate[pos] and pos not in done:
        heapq.heappush(q, ((-left + 1, -pressure), left - 1, pressure, curr_rate + rate[pos], pos, done | set([pos]), "-"))

    for n in neighbors[pos]:
        if came_from != n or len(neighbors[pos]) == 1:
            heapq.heappush(q, ((-left + 1, -pressure), left - 1, pressure, curr_rate, n, done, pos))