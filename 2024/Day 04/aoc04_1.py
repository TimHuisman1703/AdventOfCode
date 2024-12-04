file = open("aoc04_input.txt")
g = file.read().split("\n")
file.close()

xmas = "XMAS"

r = 0
for dy in range(-1, 2):
    for dx in range(-1, 2):
        for iy in range(len(g)):
            for ix in range(len(g[0])):
                x, y = ix, iy
                for i in range(4):
                    if x < 0 or x >= len(g[0]) or y < 0 or y >= len(g):
                        break
                    if g[y][x] != xmas[i]:
                        break
                    y += dy
                    x += dx
                else:
                    r += 1

print(r)