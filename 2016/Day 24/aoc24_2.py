import itertools
from heapq import heappush, heappop

class PriorityQueue():
    REMOVED = '<removed-task>'
    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.counter = itertools.count()

    def add_task(self, task, priority=0):
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def remove_task(self, task):
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop_task(self):
        while self.pq:
            priority, count, task = heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task
        return None

file = open("aoc24_input.txt")
l = file.read().split("\n")
file.close()

def a_star_length(g, src, dest):
    dist = abs(src[0] - dest[0]) + abs(src[1] - dest[1])
    queue = PriorityQueue()
    queue.add_task((src[0], src[1], 0), dist)

    while True:
        x, y, cost = queue.pop_task()
        dist = abs(x - dest[0]) + abs(y - dest[1])

        if dist == 0:
            return cost
        
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ix, iy = x + dx, y + dy
            if iy < 0 or iy > len(g)-1 or ix < 0 or ix > len(g[0])-1:
                continue

            if g[iy][ix] == 0:
                dist = abs(ix - dest[0]) + abs(iy - dest[1])
                queue.add_task((ix, iy, cost + 1), dist + cost + 1)

g = []
pos = {}

for iy in range(len(l)):
    row = []
    for ix in range(len(l[iy])):
        if l[iy][ix] == "#":
            row.append(1)
        else:
            row.append(0)
            if l[iy][ix] != ".":
                pos.update({int(l[iy][ix]): (ix, iy)})
    g.append(row)

lengths = {}
for i in range(len(pos)-1):
    for j in range(i+1, len(pos)):
        length = a_star_length(g, pos[i], pos[j])
        lengths.update({(i, j): length})
        print(f"{i} <-> {j}: {length}")

checkpoints = [*range(1, len(pos))]

minimum = 10*100

for path in itertools.permutations(checkpoints, len(checkpoints)):
    length = 0
    current = 0

    for i in range(len(path)):
        to = path[i]
        a, b = sorted([current, to])
        length += lengths[(a, b)]
        current = to
    length += lengths[(0, current)]
    
    if length < minimum:
        minimum = length

print(minimum)