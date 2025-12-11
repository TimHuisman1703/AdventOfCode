file = open("aoc11_input.txt")
l = file.read().split("\n")
file.close()

neigh = {}
for i in l:
    a, b = i.split(": ")
    neigh[a] = b.split()
    for b in b.split():
        neigh[b] = neigh.get(b, [])

topo = {}
for k, vs in neigh.items():
    topo[k] = topo.get(k, 0)
    for v in vs:
        topo[v] = topo.get(v, 0) + 1

l = [(v, k) for k, v in topo.items()]

q = [j[1] for j in l if j[0] == 0]
rs = {}
while q:
    cur = q.pop()

    if cur == "you":
        rs[cur] = 1

    for nxt in neigh[cur]:
        topo[nxt] -= 1
        rs[nxt] = rs.get(nxt, 0) + rs.get(cur, 0)
        if topo[nxt] == 0:
            q.append(nxt)

print(rs["out"])