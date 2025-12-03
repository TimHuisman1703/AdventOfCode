file = open("aoc03_input.txt")
l = file.read().split("\n")
file.close()

r = 0
for v in l:
    v = [int(j) for j in v]

    # In hindsight, DP might've been a bit of an overkill :P
    m = [[0] + [-10 ** 20] * 12 for _ in range(len(v) + 1)]
    for i in range(len(v) - 1, -1, -1):
        for k in range(1, 13):
            m[i][k] = max(m[i + 1][k], 10 ** (k - 1) * v[i] + m[i + 1][k - 1])

    r += max(max(row) for row in m)

print(r)