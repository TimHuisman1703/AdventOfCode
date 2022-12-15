file = open("aoc15_input.txt")
l = file.read().split("\n")
file.close()

Y = 2000000

c = [0 for _ in range(20000000)]

for i in l:
    i = i.split()
    sx, sy = int(i[2][2:-1]), int(i[3][2:-1])
    bx, by = int(i[8][2:-1]), int(i[9][2:])

    if by == Y:
        c[bx] = 2

    r = abs(sx - bx) + abs(by - sy)
    w = r - abs(sy - Y)
    for i in range(-w, w + 1):
        c[sx - i] = max(c[sx - i], 1)

print(c.count(1))