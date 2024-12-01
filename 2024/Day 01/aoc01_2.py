file = open("aoc01_input.txt")
l = file.read().split("\n")
file.close()

a = {}
b = {}
for x in l:
    p, q = [int(j) for j in x.split()]
    a[p] = a.get(p, 0) + 1
    b[q] = b.get(q, 0) + 1

s = 0
for p in a:
    s += p * a.get(p, 0) * b.get(p, 0)

print(s)