file = open("aoc20_input.txt")
l = file.read()[1:-1]
file.close()

import heapq

pos = [set([(0, 0)])]

right = set()
down = set()

for c in l:
    if c in "NSWE":
        new_pos = set()

        if c == "N":
            for x, y in pos[-1]:
                down.add((x, y - 1))
                new_pos.add((x, y - 1))
        elif c == "S":
            for x, y in pos[-1]:
                down.add((x, y))
                new_pos.add((x, y + 1))
        elif c == "W":
            for x, y in pos[-1]:
                right.add((x - 1, y))
                new_pos.add((x - 1, y))
        elif c == "E":
            for x, y in pos[-1]:
                right.add((x, y))
                new_pos.add((x + 1, y))
        
        pos[-1] = new_pos
    elif c == "(":
        pos.append(set())
        pos.append(pos[-2].copy())
    elif c == "|":
        pos[-2] |= pos[-1]
        pos[-1] = pos[-3].copy()
    else:
        pos[-3] = pos[-2]
        pos.pop()
        pos.pop()

q = [(0, 0, 0)]
visited = set()
c = 0

while q:
    dist, x, y = heapq.heappop(q)
    
    if (x, y) in visited:
        continue
    visited.add((x, y))

    if dist >= 1000:
        c += 1

    if (x - 1, y) in right:
        heapq.heappush(q, (dist + 1, x - 1, y))
    if (x, y) in right:
        heapq.heappush(q, (dist + 1, x + 1, y))
    if (x, y - 1) in down:
        heapq.heappush(q, (dist + 1, x, y - 1))
    if (x, y) in down:
        heapq.heappush(q, (dist + 1, x, y + 1))

print(c)