file = open("aoc18_input.txt")
l = file.read().split("\n")
file.close()

c = [tuple(int(k) for k in j.split(",")) for j in l]

v = set()
s = 6 * len(c)

for curr in c:
    v.add(curr)

    for j in range(6):
        x, y, z = [curr[k] - (k == j) + (k + 3 == j) for k in range(3)]
        if (x, y, z) in v:
            s -= 2

print(s)