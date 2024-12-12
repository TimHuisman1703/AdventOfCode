file = open("aoc12_input.txt")
g = file.read().split("\n")
file.close()

seen = [[False] * len(g[0]) for _ in range(len(g))]

r = 0
for sy in range(len(g)):
    for sx in range(len(g[0])):
        if seen[sy][sx]:
            continue

        q = [(sx, sy)]
        area = 0
        perim = 0
        while q:
            x, y = q.pop()

            if seen[y][x]:
                continue
            seen[y][x] = True
            area += 1

            for d in range(4):
                nx = x + (d == 0) - (d == 1)
                ny = y + (d == 2) - (d == 3)

                if nx < 0 or nx >= len(g[0]) or ny < 0 or ny >= len(g):
                    perim += 1
                    continue
                if g[ny][nx] != g[sy][sx]:
                    perim += 1
                    continue

                q.append((nx, ny))
    
        r += area * perim

print(r)