file = open("aoc04_input.txt")
l = file.read().split("\n")
file.close()

s = 0
for w in l:
    w = w.split(": ")[1]
    a, b = [{int(j) for j in row.split()} for row in w.split(" | ")]

    p = len(a & b)
    if p:
        s += 1 << (p - 1)

print(s)