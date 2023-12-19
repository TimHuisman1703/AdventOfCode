file = open("aoc19_input.txt")
l = file.read().split("\n\n")
file.close()

desc = l[0].split("\n")
parts = l[1].split("\n")

rules = {}
for w in desc:
    name, rule = w.split("{")
    rule = rule[:-1].split(",")
    rules[name] = rule

result = 0

q = [("in", [(1, 4000), (1, 4000), (1, 4000), (1, 4000)])]
while q:
    curr, rest = q.pop()

    if any(j[0] > j[1] for j in rest):
        continue

    if curr == "A":
        p = 1
        for a, b in rest:
            p *= b - a + 1
        result += p
        continue
    if curr == "R":
        continue

    rule = rules[curr]
    for i in range(len(rule) - 1):
        cnd, dst = rule[i].split(":")

        idx = "xmas".index(cnd[0])
        if ">" in cnd:
            threshold = int(cnd.split(">")[1])
            gone = [v if j != idx else (max(threshold + 1, v[0]), v[1]) for j, v in enumerate(rest)]
            q.append((dst, gone))
            rest = [v if j != idx else (v[0], min(threshold, v[1])) for j, v in enumerate(rest)]
        if "<" in cnd:
            threshold = int(cnd.split("<")[1])
            gone = [v if j != idx else (v[0], min(threshold - 1, v[1])) for j, v in enumerate(rest)]
            q.append((dst, gone))
            rest = [v if j != idx else (max(threshold, v[0]), v[1]) for j, v in enumerate(rest)]

    q.append((rule[-1], rest))

print(result)