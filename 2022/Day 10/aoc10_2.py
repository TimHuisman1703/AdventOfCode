file = open("aoc10_input.txt")
l = file.read().split("\n")
file.close()

i = 0
x = 1
c = 0
a = 10 ** 10

g = [["." for _ in range(40)] for _ in range(6)]

while i < len(l):
    if abs(c % 40 - x) <= 1:
        g[c // 40][c % 40] = "#"
    c += 1
    
    if a != 10 ** 10:
        x += a
        a = 10 ** 10
    else:
        if l[i] != "noop":
            a = int(l[i].split()[1])
        i += 1

print("\n".join("".join(row) for row in g))