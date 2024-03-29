file = open("aoc19_input.txt")
l = file.read().split("\n")
file.close()

from collections import deque

N = 24

s = 0

for id in range(len(l)):
    desc = l[id]
    desc = desc[desc.find(":") + 2:]
    desc = [j.replace(".", "").split() for j in desc.split(". ")]
    req = [
        [int(desc[0][4]), 0, 0, 0],
        [int(desc[1][4]), 0, 0, 0],
        [int(desc[2][4]), int(desc[2][7]), 0, 0],
        [int(desc[3][4]), 0, int(desc[3][7]), 0],
    ]
    
    max_bots = [max(req[j][0] for j in range(4)), req[2][1], req[3][2], 10 ** 10]

    q = deque([(N, (0, 0, 0, 0), (1, 0, 0, 0))])
    m = 0
    last_left = N
    dominant = []
    while q:
        left, mats, bots = q.popleft()

        curr_mats = tuple(mats[j] + bots[j] for j in range(4))

        left -= 1
        if left < last_left:
            print(f"left = {last_left}, len(q) = {len(q)}, len(dominant) = {len(dominant)}")
            last_left = left
            dominant = []
        if left == 0:
            m = max(m, curr_mats[3])
            continue

        if bots[0] > 4:
            continue

        key = (*curr_mats, *bots)
        dom = 0
        for d in dominant:
            if all(key[j] >= d[j] for j in range(8)) and any(key[j] > d[j] for j in range(8)):
                dom = 1
                break
            if all(key[j] <= d[j] for j in range(8)):
                dom = -1
                break

        if dom == 1:
            dominant = [d for d in dominant if not all(d[j] <= key[j] for j in range(8))]
        if dom == -1:
            continue

        dominant.append(key)

        for i in range(3, -1, -1):
            if bots[i] == max_bots[i]:
                continue
            for j in range(4):
                if req[i][j] > mats[j]:
                    break
            else:
                new_mats = tuple(curr_mats[j] - req[i][j] for j in range(4))
                new_bots = tuple(bots[j] + (j == i) for j in range(4))
                q.append((left, new_mats, new_bots))
        if curr_mats[0] < 7:
            q.append((left, curr_mats, bots))

    print(f"Blueprint {id + 1}: {m} geode(s)\n")
    s += m * (id + 1)

print(s)