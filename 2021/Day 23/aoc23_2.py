file = open("aoc23_input.txt")
l = file.read().split("\n")
file.close()

import heapq

def is_occupied(pos, x, y):
    if x == 0 or x == 12:
        return 4
    
    for i in range(4):
        for j in range(4):
            if pos[i][j][0] == x and pos[i][j][1] == y:
                return i
    
    return -1

def min_needed(pos):
    cost = 0

    for i in range(4):
        in_room = 0
        ix = 3 + 2 * i

        for iy in range(5, 1, -1):
            if is_occupied(pos, ix, iy) == i:
                cost += ((5 - in_room) - iy) * 10 ** i
                in_room += 1

        for j in range(4):
            if pos[i][j][0] == ix:
                continue

            cost += ((pos[i][j][1] - 1) + abs(pos[i][j][0] - ix) + (4 - in_room)) * 10 ** i
            in_room += 1
    
    return cost

pos = [[] for _ in range(4)]
for iy in range(2, 4):
    for ix in range(3, 11, 2):
        i = "ABCD".index(l[iy][ix])
        pos[i] += [(ix, 3 * (iy - 2) + 2)]

pos[0].extend([(9, 3), (7, 4)])
pos[1].extend([(7, 3), (5, 4)])
pos[2].extend([(5, 3), (9, 4)])
pos[3].extend([(3, 3), (3, 4)])

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
        for j in range(4):
            if pos[i][j][0] != 3 + 2 * i or pos[i][j][1] == 1:
                solved = False
                break
    
    if solved:
        print()
        print(cost)
        break

    for i in range(4):
        for j in range(4):
            x = pos[i][j][0]
            y = pos[i][j][1]
            for iy in range(2, 6):
                if y == iy:
                    if x == 3 + 2 * i:
                        for jy in range(iy + 1, 6):
                            if is_occupied(pos, x, jy) != i:
                                break
                        else:
                            continue
                    
                    can_get_out = True
                    for jy in range(2, iy):
                        if is_occupied(pos, x, jy) > -1:
                            can_get_out = False
                            break
                    if not can_get_out:
                        continue

                    ix = x - 1
                    while is_occupied(pos, ix + 1, 1) == -1 and is_occupied(pos, ix, 1) == -1:
                        new_pos = pos[:]
                        new_pos[i] = new_pos[i][:]
                        new_pos[i][j] = (ix, 1)
                        new_cost = cost + (iy - 1 + abs(x - ix)) * 10 ** i
                        heapq.heappush(q, (new_cost + min_needed(new_pos), new_cost, new_pos))
                        ix -= 2
                    if ix == 0 and is_occupied(pos, 1, 1) == -1:
                        new_pos = pos[:]
                        new_pos[i] = new_pos[i][:]
                        new_pos[i][j] = (1, 1)
                        new_cost = cost + (iy - 1 + abs(x - 1)) * 10 ** i
                        heapq.heappush(q, (new_cost + min_needed(new_pos), new_cost, new_pos))
                    
                    ix = x + 1
                    while is_occupied(pos, ix - 1, 1) == -1 and is_occupied(pos, ix, 1) == -1:
                        new_pos = pos[:]
                        new_pos[i] = new_pos[i][:]
                        new_pos[i][j] = (ix, 1)
                        new_cost = cost + (iy - 1 + abs(x - ix)) * 10 ** i
                        heapq.heappush(q, (new_cost + min_needed(new_pos), new_cost, new_pos))
                        ix += 2
                    if ix == 12 and is_occupied(pos, 11, 1) == -1:
                        new_pos = pos[:]
                        new_pos[i] = new_pos[i][:]
                        new_pos[i][j] = (11, 1)
                        new_cost = cost + (iy - 1 + abs(x - 11)) * 10 ** i
                        heapq.heappush(q, (new_cost + min_needed(new_pos), new_cost, new_pos))
            if y == 1:
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
                    
                    iy = 6
                    occupied_by = i
                    while occupied_by == i:
                        iy -= 1
                        occupied_by = is_occupied(pos, ix, iy)
                    
                    if occupied_by == -1:
                        new_pos = pos[:]
                        new_pos[i] = new_pos[i][:]
                        new_pos[i][j] = (ix, iy)
                        new_cost = cost + ((iy - 1) + abs(x - ix)) * 10 ** i
                        heapq.heappush(q, (new_cost + min_needed(new_pos), new_cost, new_pos))