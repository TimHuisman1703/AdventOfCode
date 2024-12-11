file = open("aoc11_input.txt")
l = [int(j) for j in file.read().split()]
file.close()

ITERATIONS = 25

d = {c: l.count(c) for c in set(l)}

for _ in range(ITERATIONS):
    nd = {}
    for c, x in d.items():
        if c == 0:
            nd[1] = nd.get(1, 0) + x
        elif len(str(c)) % 2 == 0:
            a, b = str(c)[:len(str(c)) // 2], str(c)[len(str(c)) // 2:]
            a = int(a)
            b = int(b)
            nd[a] = nd.get(a, 0) + x
            nd[b] = nd.get(b, 0) + x
        else:
            nd[2024 * c] = nd.get(2024 * c, 0) + x

    d = nd

print(sum(d.values()))