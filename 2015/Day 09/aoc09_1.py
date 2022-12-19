file = open("aoc09_input.txt")
l = [j for j in file.read().split("\n")]
file.close()

def get_shortest_next(t, a):
    a = [j for j in a]
    if t != "":
        a.remove(t)

    if len(a) == 0:
        return 0
    
    m = 10**10
    for i in a:
        m = min(m, get_shortest_next(i, a) + d[t][i])
    
    return m

d = dict()

for i in l:
    s = i.split()
    if s[0] not in d.keys():
        d.setdefault(s[0], dict())
    if s[2] not in d.keys():
        d.setdefault(s[2], dict())
    
    d[s[0]].setdefault(s[2], int(s[4]))
    d[s[2]].setdefault(s[0], int(s[4]))

t = [j for j in d.keys()]

td = dict()
for i in d.keys():
    td.setdefault(i, 0)
d.setdefault("", td)

print(get_shortest_next("", t))