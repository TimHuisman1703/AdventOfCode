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

q = [((-26, 0), 26, 0, 0, ["AA", "AA"], set(), ["-", "-"])]
v = set()

m = 26

while q:
    _, left, pressure, curr_rate, pos, done, came_from = heapq.heappop(q)

    if left < m:
        v = set()
        m = left
        print(m, pressure, len(q))

        if left == 0:
            print(pressure)
            break

    key = (*sorted([pos[0], pos[1]]), curr_rate)
    if key in v:
        continue
    v.add(key)

    pressure += curr_rate

    changes = [[], []]
    for i in range(2):
        if rate[pos[i]] and pos[i] not in done and (i == 0 or pos[0] != pos[1]):
            changes[i].append((0,))

        for n in neighbors[pos[i]]:
            if came_from[i] != n or len(neighbors[pos[i]]) == 1:
                changes[i].append((1, n))

    for a in changes[0]:
        for b in changes[1]:
            new_curr_rate = curr_rate
            new_done = done
            new_pos = pos[:]
            new_came_from = pos[:]

            for i, c in enumerate([a, b]):
                if c[0] == 0:
                    new_curr_rate += rate[pos[i]]
                    new_done = new_done | set([pos[i]])
                else:
                    new_pos[i] = c[1]
                    new_came_from[i] = pos[i]

            heapq.heappush(q, ((-left + 1, -pressure), left - 1, pressure, new_curr_rate, new_pos, new_done, new_came_from))