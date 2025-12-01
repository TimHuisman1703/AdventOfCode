file = open("aoc01_input.txt")
l = file.read().split("\n")
file.close()

s = 50
r = 0

for i in l:
    d, x = i[0], int(i[1:])

    if d == "L":
        x *= -1
    s += x

    while s < 0:
        if s - x != 0:
            r += 1
        s += 100
    while s > 100:
        if s - x != 100:
            r += 1
        s -= 100
    r += s % 100 == 0

print(r)