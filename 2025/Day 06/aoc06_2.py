file = open("aoc06_input.txt")
l = file.read().split("\n")
file.close()

indices = [j for j in range(len(l[-1])) if l[-1][j] != " "] + [len(l[-1]) + 1]
l = [[row[indices[j]:indices[j + 1] - 1] for j in range(len(indices) - 1)] for row in l]

r = 0
for i in range(len(l[0])):
    *vs, op = [row[i] for row in l]
    vs = ["".join([row[j] for row in vs]) for j in range(len(vs[0]))]
    vs = [v + op for v in vs]
    s = "".join(vs).replace(" ", "")[:-1]
    r += eval(s)

print(r)