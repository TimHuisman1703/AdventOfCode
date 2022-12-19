file = open("aoc15_input.txt")
l = file.read().split("\n")
file.close()

import heapq

g = [[int(j) for j in row] for row in l]

queue = [(0, 0, 0)]
visited = set()

while 1:
    cost, x, y = heapq.heappop(queue)

    if x == len(g[0]) - 1 and y == len(g) - 1:
        print(cost)
        break
    
    if (x, y) in visited:
        continue
    visited.add((x, y))

    for ix, iy in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if ix < 0 or ix > len(g[0]) - 1 or iy < 0 or iy > len(g) - 1:
            continue

        heapq.heappush(queue, (cost + g[iy][ix], ix, iy))