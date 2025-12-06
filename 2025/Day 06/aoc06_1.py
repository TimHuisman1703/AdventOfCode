file = open("aoc06_input.txt")
l = file.read().split("\n")
file.close()

l = [row.split() for row in l]

r = 0
for i in range(len(l[0])):
    *vs, op = [row[i] for row in l]
    vs = [v + op for v in vs]
    s = "".join(vs)[:-1]
    r += eval(s)

print(r)