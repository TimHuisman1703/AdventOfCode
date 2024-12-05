file = open("aoc05_input.txt")
o, l = file.read().split("\n\n")
file.close()

o = [[int(x) for x in j.split("|")] for j in o.split("\n")]
b = {}
for x, y in o:
    if x not in b:
        b[x] = set()
    if y not in b:
        b[y] = set()
    b[y].add(x)

r = 0
for s in l.split("\n"):
    s = [int(j) for j in s.split(",")]

    seen = set()
    for x in s:
        pos = False
        for y in seen:
            if y not in b[x]:
                pos = True
                break
        if pos:
            break
        seen.add(x)
    else:
        r += s[len(s) // 2]

print(r)