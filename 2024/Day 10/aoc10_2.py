file = open("aoc10_input.txt")
g = [[int(j) for j in row] for row in file.read().split("\n")]
file.close()

r = 0
for iy in range(len(g)):
    for ix in range(len(g[0])):
        if g[iy][ix]:
            continue

        q = [(ix, iy, set())]
        
        while q:
            x, y, visited = q.pop()

            if (x, y) in visited:
                continue
            visited = visited | set([(x, y)])

            if g[y][x] == 9:
                r += 1
                continue

            for d in range(4):
                nx = x + (d == 0) - (d == 1)
                ny = y + (d == 2) - (d == 3)

                if nx < 0 or nx >= len(g[0]) or ny < 0 or ny >= len(g):
                    continue
                if g[y][x] + 1 != g[ny][nx]:
                    continue

                q.append((nx, ny, visited))

print(r)