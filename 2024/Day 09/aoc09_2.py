file = open("aoc09_input.txt")
l = file.read().split("\n")
file.close()

import heapq

b = [[] for _ in range(10)]
q = []

s = 0
idx = 1
sc = 0
st = []
cs = []
for c in l[0]:
    c = int(c)

    if idx > 0:
        st.append(sc)
        q.append((idx, c))
        cs.append(c)
        idx = -idx
    else:
        b[c].append((len(q) - 1, sc))
        idx = -idx + 1

    sc += c

for i in range(len(q) - 1, -1, -1):
    idx, c = q.pop()

    if idx == 0:
        continue

    best = (10 ** 10, -1)
    for p in range(c, 10):
        if b[p] and b[p][0][1] < best[0] and b[p][0][0] < i:
            best = (b[p][0][1], p)
    
    if best[0] < 10 ** 10:
        j, x = heapq.heappop(b[best[1]])
        st[idx - 1] = best[0]
        heapq.heappush(b[best[1] - c], (j, x + c))

s = 0
for idx, t in enumerate(st):
    for j in range(t, t + cs[idx]):
        s += j * idx

print(s)