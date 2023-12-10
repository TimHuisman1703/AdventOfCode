file = open("aoc10_input.txt")
l = file.read().split("\n")
file.close()

visited = [[False for _ in range(len(l[0]))] for _ in range(len(l))]

for sy in range(len(l)):
    for sx in range(len(l[0])):
        if l[sy][sx] == "S":
            for d in range(4):
                q = [(
                    sx + (d == 0) - (d == 1),
                    sy + (d == 2) - (d == 3),
                    None
                )]
                locs = set([(sx, sy)])
                pos = True

                while q:
                    x, y, prev = q.pop()

                    if y < 0 or y >= len(l) or x < 0 or x >= len(l[0]) or l[y][x] == ".":
                        pos = False
                        break

                    if visited[y][x]:
                        continue
                    visited[y][x] = True
                    locs.add((x, y))

                    next = []
                    if l[y][x] == "-":
                        next = [(x - 1, y), (x + 1, y)]
                    if l[y][x] == "|":
                        next = [(x, y - 1), (x, y + 1)]
                    if l[y][x] == "L":
                        next = [(x, y - 1), (x + 1, y)]
                    if l[y][x] == "F":
                        next = [(x, y + 1), (x + 1, y)]
                    if l[y][x] == "7":
                        next = [(x, y + 1), (x - 1, y)]
                    if l[y][x] == "J":
                        next = [(x, y - 1), (x - 1, y)]
                    if l[y][x] == "S":
                        continue

                    if prev != None and prev not in next:
                        pos = False
                        break

                    q.extend([(*j, (x, y)) for j in next if j != prev])

                result = len(locs) // 2
                if pos and result:
                    print(result)
