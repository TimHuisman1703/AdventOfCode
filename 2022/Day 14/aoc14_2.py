file = open("aoc14_input.txt")
l = file.read().split("\n")
file.close()

g = [[0 for _ in range(1000)] for _ in range(200)]
my = 0

for i in l:
    c = [[int(k) for k in j.split(",")] for j in i.split(" -> ")]
    for i in range(len(c) - 1):
        x, y = c[i]
        dx, dy = c[i + 1]
        g[y][x] = 1
        while x != dx or y != dy:
            x += (x < dx) - (x > dx)
            y += (y < dy) - (y > dy)
            g[y][x] = 1
        my = max([my, y, dy])

for ix in range(len(g[0])):
    g[my + 2][ix] = 1

c = 0
while g[0][500] == 0:
    x, y = 500, 0

    while 1:
        if g[y + 1][x] == 0:
            pass
        elif g[y + 1][x - 1] == 0:
            x -= 1
        elif g[y + 1][x + 1] == 0:
            x += 1
        else:
            break
        y += 1

    c += 1
    g[y][x] = 1

print(c)