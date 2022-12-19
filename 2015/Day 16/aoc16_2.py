file = open("aoc16_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

a = []

for i in l:
    d = dict()
    s = (i+",").split()
    for j in range(2, 8, 2):
        d.setdefault(s[j][:-1], int(s[j+1][:-1]))
    a.append(d)

s = set(range(len(l)))

req_equal = {"children": 3, "samoyeds": 2, "akitas": 0, "vizslas": 0, "cars": 2, "perfumes": 1}
req_greater = {"cats": 7, "trees": 3}
req_fewer = {"pomeranians": 3, "goldfish": 5}

for i in req_equal.keys():
    ns = set(j for j in s)
    for j in s:
        try:
            if a[j][i] != req_equal[i]:
                ns.remove(j)
        except:
            pass
    s = ns
for i in req_greater.keys():
    ns = set(j for j in s)
    for j in s:
        try:
            if a[j][i] <= req_greater[i]:
                ns.remove(j)
        except:
            pass
    s = ns
for i in req_fewer.keys():
    ns = set(j for j in s)
    for j in s:
        try:
            if a[j][i] >= req_fewer[i]:
                ns.remove(j)
        except:
            pass
    s = ns

print(s)
print(f"Sue {[*s][0]+1}")