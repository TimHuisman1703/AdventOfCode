file = open("aoc06_input.txt")
l = file.read().split("\n")
file.close()

g = [[x == "#" for x in row] for row in l]

for iy in range(len(g)):
    for ix in range(len(g[0])):
        if l[iy][ix] == "^":
            x = ix
            y = iy

seen = set()
dx = 0
dy = -1
while True:
    seen.add((x, y))

    nx = x + dx
    ny = y + dy
    if nx < 0 or nx >= len(g[0]) or ny < 0 or ny >= len(g):
        break

    if g[ny][nx]:
        dx, dy = -dy, dx
        continue

    x, y = nx, ny

print(len(seen))