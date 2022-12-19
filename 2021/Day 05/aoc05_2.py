file = open("aoc05_input.txt")
l = file.read().split("\n")
file.close()

min_x = min_y = 100000
max_x = max_y = -100000

for i in l:
    a, b = i.split(" -> ")
    c, d = map(int, b.split(","))
    a, b = map(int, a.split(","))
    
    min_y = min(min_y, b, d)
    max_y = max(max_y, b, d)
    min_x = min(min_x, a, c)
    max_x = max(max_x, a, c)

g = [[0 for ix in range(max_x - min_x + 1)] for iy in range(max_y - min_y + 1)]

for i in l:
    a, b = i.split(" -> ")
    c, d = map(int, b.split(","))
    a, b = map(int, a.split(","))

    if a == c:
        b, d = sorted([b, d])
        for iy in range(b, d + 1):
            g[iy - min_y][a - min_x] += 1
    if b == d:
        a, c = sorted([a, c])
        for ix in range(a, c + 1):
            g[b - min_y][ix - min_x] += 1
    
    if a - c == b - d:
        a, c = sorted([a, c])
        b, d = sorted([b, d])
        for i in range((c - a) + 1):
            g[b + i - min_y][a + i - min_x] += 1
    
    if a - c == d - b:
        a, c = sorted([a, c])
        d, b = sorted([b, d])
        for i in range((c - a) + 1):
            g[b - i - min_y][a + i - min_x] += 1    

c = 0
for row in g:
    for i in row:
        if i > 1:
            c += 1

print(c)