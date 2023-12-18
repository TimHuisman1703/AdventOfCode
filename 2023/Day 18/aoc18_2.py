file = open("aoc18_input.txt")
l = file.read().split("\n")
file.close()

corners = []
edge = 0
x = y = 0
for w in l:
    d, s, c = w.split()
    d = "RDLU"[int(c[7])]
    s = int(c[2:7], 16)

    edge += s

    x += ((d == "R") - (d == "L")) * s
    y += ((d == "D") - (d == "U")) * s

    corners.append((x, y))

area = 0
for i in range(len(corners) - 2):
    a, b = corners[i], corners[i + 1]
    area += (a[0] * b[1] - b[0] * a[1]) // 2

print(abs(area) + edge // 2 + 1)