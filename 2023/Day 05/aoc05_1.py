file = open("aoc05_input.txt")
l = file.read().split("\n\n")
file.close()

l = [j.split("\n") for j in l]
seeds = [int(j) for j in l[0][0].split(": ")[1].split()]

for w in l[1:]:
    ranges = [[int(j) for j in row.split()] for row in w[1:]]

    ns = []
    for s in seeds:
        for a, b, c in ranges:
            if b <= s and s < b + c:
                ns.append(s + a - b)
                break
        else:
            ns.append(s)
    seeds = ns

print(min(seeds))