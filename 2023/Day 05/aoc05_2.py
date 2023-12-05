file = open("aoc05_input.txt")
l = file.read().split("\n\n")
file.close()

l = [j.split("\n") for j in l]
seeds = [int(j) for j in l[0][0].split(": ")[1].split()]
seeds = [[seeds[2 * j], seeds[2 * j] + seeds[2 * j + 1] - 1] for j in range(len(seeds) // 2)]

for w in l[1:]:
    ranges = [[int(j) for j in row.split()] for row in w[1:]]

    ns = []
    for a, b, c in ranges:
        os = []
        for p, q in seeds:
            np = max(p, b)
            nq = min(q, b + c - 1)
            if np <= nq:
                ns.append([np + a - b, nq + a - b])
                if p <= np - 1:
                    os.append([p, np - 1])
                if nq + 1 <= q:
                    os.append([nq + 1, q])
            else:
                os.append([p, q])
        seeds = os
    seeds = os + ns

print(min(seeds)[0])