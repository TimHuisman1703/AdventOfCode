file = open("aoc04_input.txt")
l = file.read().split("\n")
file.close()

d = [1] * len(l)
for idx, w in enumerate(l):
    w = w.split(": ")[1]
    a, b = [{int(j) for j in row.split()} for row in w.split(" | ")]

    p = len(a & b)
    for i in range(idx + 1, idx + 1 + p):
        d[i] += d[idx]

print(sum(d))