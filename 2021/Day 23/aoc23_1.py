file = open("aoc23_input.txt")
l = file.read().split("\n")
file.close()

import heapq

def is_occupied(pos, x, y):
    if x == 0 or x == 12:
        return 4
    
    for i in range(4):
        for j in range(2):
            if pos[i][j][0] == x and pos[i][j][1] == y:
                return i
    
    return -1

def min_needed(pos):
    cost = 0

    for i in range(4):
        in_room = 0
        ix = 3 + 2 * i

        for iy in range(3, 1, -1):
            if is_occupied(pos, ix, iy) == i:
                cost += ((5 - in_room) - iy) * 10 ** i
                in_room += 1

        for j in range(2):
            if pos[i][j][0] == ix:
                continue

            cost += ((pos[i][j][1] - 1) + abs(pos[i][j][0] - ix) + (2 - in_room)) * 10 ** i
            in_room += 1
    
    return cost

pos = [[] for _ in range(4)]
for iy in range(2, 4):
    for ix in range(3, 11, 2):
        i = "ABCD".index(l[iy][ix])
        pos[i] += [(ix, iy)]

q = [(0, 0, pos)]
visited = set()

ma = 0

while 1:
    _, cost, pos = heapq.heappop(q)

    string = str(pos)
    if string in visited:
        continue
    visited.add(string)

    if cost // 1000 > ma // 1000:
        ma = cost
        print(cost)

    solved = True
    for i in range(4):
        for j in range(2):
            if pos[i][j][0] != 3 + 2 * i or pos[j][0][1] == 1:
                solved = False
                break
    
    if solved:
        print()
        print(cost)
        break

    for i in range(4):
        for j in range(2):
            x = pos[i][j][0]
            y = pos[i][j][1]
            if y == 3:
                if x == 3 + 2 * i:
                    continue

                if is_occupied(pos, x, 2) == -1:
                    ix = x - 1
                    while is_occupied(pos, ix + 1, 1) == -1 and is_occupied(pos, ix, 1) == -1:
                        new_pos = pos[:]
                        new_pos[i] = new_pos[i][:]
                        new_pos[i][j] = (ix, 1)
                        new_cost = cost + (2 + abs(x - ix)) * 10 ** i
                        heapq.heappush(q, (new_cost + min_needed(new_pos), new_cost, new_pos))
                        ix -= 2
                    if ix == 0 and is_occupied(pos, 1, 1) == -1:
                        new_pos = pos[:]
                        new_pos[i] = new_pos[i][:]
                        new_pos[i][j] = (1, 1)
                        new_cost = cost + (2 + abs(x - 1)) * 10 ** i
                        heapq.heappush(q, (new_cost + min_needed(new_pos), new_cost, new_pos))
                    
                    ix = x + 1
                    while is_occupied(pos, ix - 1, 1) == -1 and is_occupied(pos, ix, 1) == -1:
                        new_pos = pos[:]
                        new_pos[i] = new_pos[i][:]
                        new_pos[i][j] = (ix, 1)
                        new_cost = cost + (2 + abs(x - ix)) * 10 ** i
                        heapq.heappush(q, (new_cost + min_needed(new_pos), new_cost, new_pos))
                        ix += 2
                    if ix == 12 and is_occupied(pos, 11, 1) == -1:
                        new_pos = pos[:]
                        new_pos[i] = new_pos[i][:]
                        new_pos[i][j] = (11, 1)
                        new_cost = cost + (2 + abs(x - 11)) * 10 ** i
                        heapq.heappush(q, (new_cost + min_needed(new_pos), new_cost, new_pos))
            elif y == 2:
                if x == 3 + 2 * i and is_occupied(pos, x, 3) == i:
                    continue

                ix = x - 1
                while is_occupied(pos, ix + 1, 1) == -1 and is_occupied(pos, ix, 1) == -1:
                    new_pos = pos[:]
                    new_pos[i] = new_pos[i][:]
                    new_pos[i][j] = (ix, 1)
                    new_cost = cost + (1 + abs(x - ix)) * 10 ** i
                    heapq.heappush(q, (new_cost + min_needed(new_pos), new_cost, new_pos))
                    ix -= 2
                if ix == 0 and is_occupied(pos, 1, 1) == -1:
                    new_pos = pos[:]
                    new_pos[i] = new_pos[i][:]
                    new_pos[i][j] = (1, 1)
                    new_cost = cost + (1 + abs(x - 1)) * 10 ** i
                    heapq.heappush(q, (new_cost + min_needed(new_pos), new_cost, new_pos))
                
                ix = x + 1
                while is_occupied(pos, ix - 1, 1) == -1 and is_occupied(pos, ix, 1) == -1:
                    new_pos = pos[:]
                    new_pos[i] = new_pos[i][:]
                    new_pos[i][j] = (ix, 1)
                    new_cost = cost + (1 + abs(x - ix)) * 10 ** i
                    heapq.heappush(q, (new_cost + min_needed(new_pos), new_cost, new_pos))
                    ix += 2
                if ix == 12 and is_occupied(pos, 11, 1) == -1:
                    new_pos = pos[:]
                    new_pos[i] = new_pos[i][:]
                    new_pos[i][j] = (11, 1)
                    new_cost = cost + (1 + abs(x - 11)) * 10 ** i
                    heapq.heappush(q, (new_cost + min_needed(new_pos), new_cost, new_pos))
            elif y == 1:
                ix = 3 + 2 * i
                if is_occupied(pos, ix, 2) == -1:
                    available = True
                    jx = x
                    while jx != ix:
                        if jx < ix:
                            jx += 1
                        else:
                            jx -= 1
                        
                        if is_occupied(pos, jx, 1) > -1:
                            available = False
                            break
                    
                    if not available:
                        continue
                    
                    occupied_by = is_occupied(pos, ix, 3)
                    if occupied_by == -1:
                        new_pos = pos[:]
                        new_pos[i] = new_pos[i][:]
                        new_pos[i][j] = (ix, 3)
                        new_cost = cost + (2 + abs(x - ix)) * 10 ** i
                        heapq.heappush(q, (new_cost + min_needed(new_pos), new_cost, new_pos))
                    if occupied_by == i:
                        new_pos = pos[:]
                        new_pos[i] = new_pos[i][:]
                        new_pos[i][j] = (ix, 2)
                        new_cost = cost + (1 + abs(x - ix)) * 10 ** i
                        heapq.heappush(q, (new_cost + min_needed(new_pos), new_cost, new_pos))