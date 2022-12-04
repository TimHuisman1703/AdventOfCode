file = open("aoc04_input.txt")
l = file.read().split("\n")
file.close()

s = 0

for i in l:
    p, q = i.split(",")
    a = [int(j) for j in p.split("-")]
    b = [int(j) for j in q.split("-")]

    a, b = sorted([a, b], key=lambda x: (x[0], -x[1]))
    s += b[1] <= a[1]

print(s)