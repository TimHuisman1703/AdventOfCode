file = open("aoc07_input.txt")
l = file.read().split("\n")
file.close()

types = "AKQT98765432J"

cs = []
for w in l:
    h, s = w.split()
    s = int(s)

    inst = []
    for t in types[:-1]:
        p = h.count(t)
        if p:
            inst.append((p, t))

    inst = sorted(inst, key=lambda x: -x[0])
    if h == "JJJJJ":
        inst = [(5, "A")]
    else:
        inst[0] = (inst[0][0] + h.count("J"), inst[0][1])
    inst = ([x[0] for x in inst], [types.index(x) for x in h])
    cs.append((inst, s))

for _ in range(len(l)):
    for i in range(len(l) - 1):
        a = cs[i][0]
        b = cs[i + 1][0]

        if a[0] > b[0]:
            cs[i], cs[i + 1] = cs[i + 1], cs[i]
        elif a[0] == b[0] and a[1] < b[1]:
            cs[i], cs[i + 1] = cs[i + 1], cs[i]

s = sum([(j + 1) * cs[j][1] for j in range(len(cs))])

print(s)