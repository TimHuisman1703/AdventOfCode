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

    s %= 100
    r += s == 0

print(r)