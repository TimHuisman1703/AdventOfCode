file = open("aoc03_input.txt")
l = file.read().split("\n")
file.close()

r = 0
for v in l:
    v = [int(j) for j in v]

    a = max(v[:-1])
    idx = v.index(a)
    b = max(v[idx + 1:])

    r += 10 * a + b

print(r)