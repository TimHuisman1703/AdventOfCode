file = open("aoc01_input.txt")
l = file.read().split("\n")
file.close()

a = []
b = []
for x in l:
    p, q = [int(j) for j in x.split()]
    a.append(p)
    b.append(q)

a = sorted(a)
b = sorted(b)

s = 0
for p, q in zip(a, b):
    s += abs(p - q)

print(s)