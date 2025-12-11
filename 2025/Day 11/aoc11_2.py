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

    if cur == "svr":
        rs[cur] = [1, 0, 0, 0]

    for nxt in neigh[cur]:
        topo[nxt] -= 1

        rscur = rs.get(cur, [0, 0, 0, 0])
        rsnxt = rs.get(nxt, [0, 0, 0, 0])
        for i in range(4):
            rsnxt[i] += rscur[i]

        if nxt == "fft":
            rsnxt[1] += rsnxt[0]
            rsnxt[3] += rsnxt[2]
            rsnxt[0] = rsnxt[2] = 0
        if nxt == "dac":
            rsnxt[2] += rsnxt[0]
            rsnxt[3] += rsnxt[1]
            rsnxt[0] = rsnxt[1] = 0
        
        rs[nxt] = rsnxt

        if topo[nxt] == 0:
            q.append(nxt)

print(rs["out"][3])